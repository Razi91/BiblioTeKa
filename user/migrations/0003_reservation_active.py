# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150601_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
