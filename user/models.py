
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
 
 
__author__ = 'jkonieczny'
 
 
class Subscription(models.Model):
    name = models.CharField(max_length=32)
    initial = models.DecimalField(max_digits=5, decimal_places=2)
    monthly = models.DecimalField(max_digits=5, decimal_places=2)
 
 
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
    begin = models.DateField(default=datetime.now)
    end = models.DateField()
 
 
class Loan(models.Model):
    client = models.ForeignKey('Client')
    book = models.ForeignKey('books.BookEntity')
    date = models.DateTimeField(default=datetime.now)
    returned = models.DateTimeField()
    subscription = models.ForeignKey('SubscriptionActive')