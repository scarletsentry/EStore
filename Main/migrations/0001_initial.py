# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ssno', models.CharField(unique=True, max_length=100, blank=True)),
                ('first_name', models.CharField(max_length=100, blank=True)),
                ('last_name', models.CharField(max_length=100, blank=True)),
                ('email', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=50)),
                ('storeCredit', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('accessLevel', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('isFinalized', models.BooleanField(default=False)),
                ('totalPrice', models.FloatField()),
                ('customer', models.ForeignKey(to='Main.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=255, null=True, blank=True)),
                ('info', models.TextField(null=True, blank=True)),
                ('contactInfo', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('listingPrice', models.FloatField()),
                ('currentPrice', models.FloatField()),
                ('info', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('manufacturer', models.ForeignKey(to='Main.Manufacturer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField(default=-1.0)),
                ('invoice', models.ForeignKey(to='Main.Invoice')),
                ('product', models.ForeignKey(to='Main.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('reason', models.TextField()),
                ('invoice', models.ForeignKey(to='Main.Invoice')),
                ('product', models.ForeignKey(to='Main.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('contactInfo', models.TextField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(to='Main.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(to='Main.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('contactInfo', models.TextField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='stock',
            name='store',
            field=models.ForeignKey(to='Main.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='store',
            field=models.ForeignKey(to='Main.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='supplier',
            field=models.ForeignKey(to='Main.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='serviceCenter',
            field=models.ForeignKey(to='Main.ServiceCenter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(to='Main.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='store',
            field=models.ForeignKey(to='Main.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='worksAt',
            field=models.ForeignKey(to='Main.Store'),
            preserve_default=True,
        ),
    ]
