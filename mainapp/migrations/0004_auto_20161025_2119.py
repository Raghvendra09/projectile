# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 21:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20161025_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='u_bio',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='u_contact_no',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
