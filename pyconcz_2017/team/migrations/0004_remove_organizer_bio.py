# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-08-23 05:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20160823_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizer',
            name='bio',
        ),
    ]
