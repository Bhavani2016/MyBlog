# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 16:49
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20170913_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='images/category'),
        ),
    ]
