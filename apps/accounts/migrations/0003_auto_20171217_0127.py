# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 06:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20171216_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Cuenta'},
        ),
    ]