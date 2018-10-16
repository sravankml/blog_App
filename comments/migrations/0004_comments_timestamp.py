# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20180819_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
