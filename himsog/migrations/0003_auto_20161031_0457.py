# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-31 04:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('himsog', '0002_auto_20160924_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentimage',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='contentimage',
            name='rating',
        ),
    ]
