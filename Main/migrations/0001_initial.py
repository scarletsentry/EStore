# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=50)),
                ('storeCredit', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('accessLevel', models.IntegerField()),
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
                ('totalPrice', models.FloatField()),
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
                ('logo', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('contactInfo', models.TextField()),
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
                ('customer', models.ForeignKey(to='Main.Customer')),
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
                ('customer', models.ForeignKey(to='Main.Customer')),
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
                ('contactInfo', models.TextField()),
                ('address', models.TextField()),
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
                ('contactInfo', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='stock',
            name='supplier',
            field=models.ForeignKey(to='Main.Supplier'),
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
            model_name='employee',
            name='worksAt',
            field=models.ForeignKey(to='Main.Store'),
            preserve_default=True,
        ),
    ]
