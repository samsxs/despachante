# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recibo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Nome'),
        ),
    ]
