# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 15:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0004_auto_20180515_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-post_date']},
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.Image'),
        ),
        migrations.AddField(
            model_name='comments',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]