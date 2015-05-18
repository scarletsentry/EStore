# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='supplier',
        ),
        migrations.AddField(
            model_name='stock',
            name='store',
            field=models.ForeignKey(default=None, to='Main.Store'),
            preserve_default=False,
        ),
    ]
