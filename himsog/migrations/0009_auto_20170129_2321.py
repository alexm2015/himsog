# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-29 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('himsog', '0008_auto_20170129_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentimage',
            name='is_primary',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
