# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 18:45
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bored', '0002_contents_discriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='Discriptions',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
