# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bored', '0011_contents_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]