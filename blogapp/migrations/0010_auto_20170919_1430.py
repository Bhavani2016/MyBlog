# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='body',
        ),
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=True),
        ),
    ]