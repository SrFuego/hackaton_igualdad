# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-16 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dni',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
