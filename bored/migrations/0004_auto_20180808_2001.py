# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 20:01
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bored', '0003_auto_20180808_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='Discriptions',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]