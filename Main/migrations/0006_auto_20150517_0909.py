# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20150517_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='return',
            name='customer',
        ),
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
