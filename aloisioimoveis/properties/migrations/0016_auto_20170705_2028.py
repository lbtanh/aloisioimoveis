# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0015_auto_20170701_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='conditions',
            field=models.CharField(blank=True, max_length=100, verbose_name='condições'),
        ),
    ]
