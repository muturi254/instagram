# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0007_auto_20180515_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='likes',
            new_name='users_liked',
        ),
    ]
