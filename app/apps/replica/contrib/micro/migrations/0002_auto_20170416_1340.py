# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='deck',
            field=models.TextField(blank=True, verbose_name='deck'),
        ),
        migrations.AddField(
            model_name='timeline',
            name='deck_html',
            field=models.TextField(blank=True),
        ),
    ]
