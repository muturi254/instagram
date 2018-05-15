# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 10:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts/')),
                ('image_name', models.CharField(max_length=30)),
                ('image_caption', models.TextField(blank=True)),
                ('image_likes', models.PositiveIntegerField(default=0)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='avatar')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
