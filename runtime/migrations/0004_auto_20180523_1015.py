# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-23 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('predModels', '0005_auto_20180523_1015'),
        ('runtime', '0003_auto_20180507_0756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xtrace',
            old_name='results',
            new_name='class_results',
        ),
        migrations.RemoveField(
            model_name='xtrace',
            name='model',
        ),
        migrations.AddField(
            model_name='xtrace',
            name='class_model',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='class_trace_model', to='predModels.PredModels'),
        ),
        migrations.AddField(
            model_name='xtrace',
            name='reg_model',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reg_trace_model', to='predModels.PredModels'),
        ),
        migrations.AddField(
            model_name='xtrace',
            name='reg_results',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
