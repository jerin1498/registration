# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-10-23 18:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_registration_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='contact_no',
        ),
    ]
