from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
 
 
__author__ = 'jkonieczny'
 
 
class Subscription(models.Model):
    name = models.CharField(max_length=32)
    prize = models.DecimalField(max_digits=5, decimal_places=2)
    credits = models.DecimalField(max_digits=5, decimal_places=2)

class ClientManager(models.Manager):
    def get_query(self):
        return super(ClientManager, self).select_related('User')
 
 
class Client(models.Model):
    user = models.ForeignKey(User, null=False)
    birthday = models.DateField()
    pesel = models.CharField(max_length=11)
    credits = models.DecimalField(max_digits=5, decimal_places=2)
    
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
 
class Staff(models.Model):
    user = models.ForeignKey(User, null=False)
 
 
class SubscriptionActive(models.Model):
    client = models.ForeignKey('Client')
    subscription = models.ForeignKey('Subscription')
    credits = models.DecimalField(max_digits=5, decimal_places=2)
    begin = models.DateField(default=datetime.now)
    end = models.DateField()
 
 
class Loan(models.Model):
    client = models.ForeignKey('Client', related_name="loans")
    book = models.ForeignKey('books.BookEntity')
    date = models.DateTimeField(default=datetime.now)
    returned = models.DateTimeField()
    pricing = models.ForeignKey('Pricing')
    subscription = models.ForeignKey('SubscriptionActive')