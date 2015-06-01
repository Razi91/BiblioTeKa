from django.db import models
from user.models import *
from django.contrib import admin


class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'pesel', 'credits')
admin.site.register(Client, ClientAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'prize', 'credits')
admin.site.register(Subscription, SubscriptionAdmin)

class SubscriptionActiveAdmin(admin.ModelAdmin):
    list_display = ('client', 'credits', 'subscription', 'begin', 'end')
admin.site.register(SubscriptionActive, SubscriptionActiveAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('client', 'book', 'date', 'returned', 'pricing')
admin.site.register(Loan, LoanAdmin)

