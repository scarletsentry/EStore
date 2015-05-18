# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20150516_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='contactInfo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='logo',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
