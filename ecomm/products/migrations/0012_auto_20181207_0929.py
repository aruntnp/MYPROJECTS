# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-07 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_productdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdetail',
            old_name='product_size',
            new_name='product_size_available',
        ),
    ]
