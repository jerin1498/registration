# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-10-23 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0005_auto_20191018_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='live',
            name='madpyrate_fb_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='live',
            name='madpyrate_twiter_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
