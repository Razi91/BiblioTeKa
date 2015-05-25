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
 
class Staff(models.Model):
    user = models.ForeignKey(User, null=False)
 
 
class SubscriptionActive(models.Model):
    client = models.ForeignKey('Client')
    subscription = models.ForeignKey('Subscription')
    credits = models.DecimalField(max_digits=5, decimal_places=2)
    begin = models.DateField(default=datetime.now)
    end = models.DateField()
 
 
class Loan(models.Model):
    client = models.ForeignKey('Client')
    book = models.ForeignKey('books.BookEntity')
    date = models.DateTimeField(default=datetime.now)
    returned = models.DateTimeField()
    subscription = models.ForeignKey('SubscriptionActive')