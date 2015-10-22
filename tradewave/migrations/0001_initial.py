# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('amount_issued', models.FloatField()),
                ('amount_redeemed', models.FloatField()),
                ('series', models.IntegerField()),
                ('credit_rating', models.FloatField()),
                ('date_created', models.DateTimeField(verbose_name=b'date created')),
                ('date_expire', models.DateTimeField(verbose_name=b'date to expire')),
                ('date_lastspent', models.DateTimeField(verbose_name=b'date last transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Marketplace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField()),
                ('date_active', models.DateTimeField()),
                ('num_members', models.IntegerField(verbose_name=b'number of members')),
                ('city', models.ForeignKey(to='tradewave.City')),
            ],
        ),
        migrations.CreateModel(
            name='MarketplaceAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admin_for', models.ForeignKey(to='tradewave.Marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='MarketplaceManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manager_for', models.ForeignKey(to='tradewave.Marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='MarketplaceProperty',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('marketplace_rating', models.FloatField()),
                ('credit_ceiling', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MarketplaceVendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marketplace', models.ForeignKey(to='tradewave.Marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='MarketplaceVenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marketplace', models.ForeignKey(to='tradewave.Marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(verbose_name=b'transaction timestamp')),
                ('amount', models.FloatField()),
                ('redeemed', models.BooleanField()),
                ('credit', models.ForeignKey(to='tradewave.Credit')),
            ],
        ),
        migrations.CreateModel(
            name='UserProperty',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_created', models.DateTimeField(verbose_name=b'date joined')),
                ('date_active', models.DateTimeField(verbose_name=b'date last active')),
                ('is_vendor', models.BooleanField()),
                ('is_marketplace', models.BooleanField()),
                ('pin', models.IntegerField()),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='VendorAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorProperty',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('vendor_rating', models.FloatField()),
                ('credit_ceiling', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='VendorVenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField()),
                ('date_active', models.DateTimeField()),
                ('city', models.ForeignKey(to='tradewave.City')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('credit', models.ForeignKey(to='tradewave.Credit')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='vendorvenue',
            name='venue',
            field=models.ForeignKey(to='tradewave.Venue'),
        ),
        migrations.AddField(
            model_name='vendormanager',
            name='manager_for',
            field=models.ForeignKey(related_name='vendor_managed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vendormanager',
            name='user',
            field=models.ForeignKey(related_name='vendor_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vendoradmin',
            name='admin_for',
            field=models.ForeignKey(related_name='vendor_administered', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vendoradmin',
            name='user',
            field=models.ForeignKey(related_name='vendor_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transactionlog',
            name='venue',
            field=models.ForeignKey(to='tradewave.Venue'),
        ),
        migrations.AddField(
            model_name='transactionlog',
            name='wallet_receive',
            field=models.ForeignKey(related_name='receiver', to='tradewave.Wallet'),
        ),
        migrations.AddField(
            model_name='transactionlog',
            name='wallet_send',
            field=models.ForeignKey(related_name='sender', to='tradewave.Wallet'),
        ),
        migrations.AddField(
            model_name='marketplacevenue',
            name='venue',
            field=models.ForeignKey(to='tradewave.Venue'),
        ),
        migrations.AddField(
            model_name='marketplacevendor',
            name='vendor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='marketplacemanager',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='marketplaceadmin',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='credit',
            name='issuer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
