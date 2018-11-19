# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-27 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=100),
        ),
    ]