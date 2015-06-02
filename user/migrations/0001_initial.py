# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('birthday', models.DateField()),
                ('pesel', models.CharField(max_length=11)),
                ('credits', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user', models.OneToOneField(related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('returned', models.DateTimeField(null=True)),
                ('book', models.ForeignKey(to='books.BookEntity')),
                ('client', models.ForeignKey(related_name='loans', to='user.Client')),
                ('pricing', models.ForeignKey(to='books.Pricing')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('book', models.ForeignKey(to='books.BookEdition', null=True)),
                ('client', models.ForeignKey(related_name='reservations', to='user.Client')),
                ('pricing', models.ForeignKey(to='books.Pricing')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('prize', models.DecimalField(decimal_places=2, max_digits=5)),
                ('credits', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionActive',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('credits', models.DecimalField(decimal_places=2, max_digits=5)),
                ('begin', models.DateField(default=datetime.datetime.now)),
                ('end', models.DateField()),
                ('client', models.ForeignKey(to='user.Client')),
                ('subscription', models.ForeignKey(to='user.Subscription')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='subscription',
            field=models.ForeignKey(to='user.SubscriptionActive', null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='title',
            field=models.ForeignKey(to='books.BookTitle'),
        ),
        migrations.AddField(
            model_name='loan',
            name='subscription',
            field=models.ForeignKey(to='user.SubscriptionActive', null=True),
        ),
    ]
