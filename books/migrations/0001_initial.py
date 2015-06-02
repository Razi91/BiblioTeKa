# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('born', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BookEdition',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('release', models.DateTimeField()),
                ('isbn', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='BookEntity',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('quality', models.IntegerField()),
                ('book', models.ForeignKey(related_name='entities', to='books.BookEdition')),
            ],
        ),
        migrations.CreateModel(
            name='BookTitle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('release', models.DateTimeField()),
                ('title', models.CharField(max_length=256)),
                ('author', models.ManyToManyField(to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('initial', models.DecimalField(decimal_places=2, max_digits=5)),
                ('per_week', models.DecimalField(decimal_places=2, max_digits=5)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('closed', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='booktitle',
            name='genre',
            field=models.ManyToManyField(to='books.Genre'),
        ),
        migrations.AddField(
            model_name='bookentity',
            name='title',
            field=models.ForeignKey(to='books.BookTitle'),
        ),
        migrations.AddField(
            model_name='bookedition',
            name='pricing',
            field=models.ForeignKey(null=True, blank=True, to='books.Pricing'),
        ),
        migrations.AddField(
            model_name='bookedition',
            name='publisher',
            field=models.ForeignKey(to='books.Publisher'),
        ),
        migrations.AddField(
            model_name='bookedition',
            name='title',
            field=models.ForeignKey(related_name='publications', to='books.BookTitle'),
        ),
    ]
