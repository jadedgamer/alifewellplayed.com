# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulse', '0011_auto_20170907_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=510),
        ),
    ]