# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('pesel', models.CharField(max_length=11)),
                ('credits', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('returned', models.DateTimeField()),
                ('book', models.ForeignKey(to='books.BookEntity')),
                ('client', models.ForeignKey(to='user.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('initial', models.DecimalField(decimal_places=2, max_digits=5)),
                ('monthly', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionActive',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(default=datetime.datetime.now)),
                ('end', models.DateField()),
                ('client', models.ForeignKey(to='user.Client')),
                ('subscription', models.ForeignKey(to='user.Subscription')),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='subscription',
            field=models.ForeignKey(to='user.SubscriptionActive'),
        ),
    ]
