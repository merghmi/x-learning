# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-06 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_fss', '0005_auto_20160306_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cin',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
