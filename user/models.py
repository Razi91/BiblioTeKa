from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta
from django.db.models import Q
from books.models import *
from math import *
 
__author__ = 'jkonieczny'
 
 
class Subscription(models.Model):
    name = models.CharField(max_length=32)
    prize = models.DecimalField(max_digits=5, decimal_places=2)
    credits = models.DecimalField(max_digits=5, decimal_places=2)

class ClientManager(models.Manager):
    def get_query(self):
        return super(ClientManager, self).select_related('User')
 
 
class Client(models.Model):
    user = models.OneToOneField(User, null=False, related_name='client')
    birthday = models.DateField()
    pesel = models.CharField(max_length=11)
    credits = models.DecimalField(max_digits=5, decimal_places=2)

    def active_loans(self):
        return self.loans.filter(returned__isnull=True)
    def active_reservations(self):
        return self.reservations.filter(active=True)

    
    def saldo(self):
        now = datetime.datetime.now()
        c = self.credits
        loans = self.loans.filter(end__isnull=True).select_related('subscription')
        subs = {}
        for l in loans:
            sub = None
            if l.subscription is not None:
                if l.subscription.id not in subs:
                    sub = l.subscription
                    subs[l.subscription.id] = l.subscription
                else:
                    sub = subs[l.subscription.id]
            if sub is None:
                c -= l.pricing.initial
                weeks = ceil((now - l.begin).seconds*1.0 / 60/60/24/7)
                c -= weeks * l.pricing.per_week
            else:
                sub.credits -= l.pricing.initial
                weeks = ceil((now - l.begin).seconds*1.0 / 60/60/24/7)
                sub.credits -= weeks * l.pricing.per_week
        for id, sub in subs.items():
            c += min(0, sub.credits)
        return c

    def current_subscriptions(self):
        subs = SubscriptionActive.objects.filter(client=self)
 
class Staff(models.Model):
    user = models.ForeignKey(User, null=False)
 
 
class SubscriptionActive(models.Model):
    client = models.ForeignKey('Client')
    subscription = models.ForeignKey('Subscription')
    credits = models.DecimalField(max_digits=5, decimal_places=2)
    begin = models.DateField(default=datetime.now)
    end = models.DateField()

    @property
    def loads(self):
        loans = Loan.objects.filter(subscription=self, returned__isnull=True)
        s = 0
        for l in loans:
            s += l.current_fee
        return s
 
 
class Loan(models.Model):
    client = models.ForeignKey('Client', related_name="loans")
    book = models.ForeignKey('books.BookEntity')
    date = models.DateTimeField(default=datetime.now)
    returned = models.DateTimeField(null=True)
    pricing = models.ForeignKey('books.Pricing')
    subscription = models.ForeignKey('SubscriptionActive', null=True)

    @property
    def current_fee(self):
        weeks = ceil((datetime.now().date() - self.date.date() + timedelta(seconds=1)).seconds/(60.0*60*24*7))
        fee = weeks * self.pricing.per_week
        return fee

    def loan(self, cred):
        cred.credits -= self.pricing.initial

    def find_reserv(self):
        res = Reservation.objects.filter(title=self.book.title).filter(Q(book=self)|Q(book_isnull=True))\
            .order_by('date')
        return res.first()

    def back(self):
        if self.subscription is not None:
            cred = self.subscription
        else:
            cred = self.client
        cred.credits += self.pricing.initial
        fee = self.current_fee
        cred.credits -= fee

        if self.subscription is not None:
            if cred.credits < 0:
                self.client.credits += cred.credits
                cred.credits = 0
        self.returned = datetime.now().date()

class Reservation(models.Model):
    client = models.ForeignKey('Client', related_name="reservations")
    active = models.BooleanField(default=True)
    book = models.ForeignKey('books.BookEdition', null=True)
    title = models.ForeignKey('books.BookTitle')
    date = models.DateTimeField(default=datetime.now)
    pricing = models.ForeignKey('books.Pricing', null=True)
    subscription = models.ForeignKey('SubscriptionActive', null=True)