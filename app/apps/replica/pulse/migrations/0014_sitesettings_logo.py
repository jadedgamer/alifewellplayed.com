# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pulse', '0013_auto_20170907_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pulse.Media'),
        ),
    ]
