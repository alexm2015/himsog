# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-01 00:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('himsog', '0005_auto_20161031_0608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='content',
            name='rating',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]