# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20150516_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='customer',
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(default=0, to='Main.Customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='store',
            field=models.ForeignKey(default=0, to='Main.Store'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicecenter',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servicecenter',
            name='contactInfo',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contactInfo',
            field=models.TextField(null=True, blank=True),
        ),
    ]
