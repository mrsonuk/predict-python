# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-03 19:59
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='properties',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
