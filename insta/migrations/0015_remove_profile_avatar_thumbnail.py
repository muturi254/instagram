# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0014_auto_20180515_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar_thumbnail',
        ),
    ]