# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_auto_20150517_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='isFinalized',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
