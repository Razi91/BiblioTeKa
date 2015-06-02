# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookentity_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookentity',
            name='uuid',
            field=models.CharField(max_length=40),
        ),
    ]
