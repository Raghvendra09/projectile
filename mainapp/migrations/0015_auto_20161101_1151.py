# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20161101_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='u_education_end_year',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='u_education_start_year',
            field=models.CharField(max_length=4),
        ),
    ]
