# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 13:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedIp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128)),
                ('ip_addr', models.GenericIPAddressField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Blocked IP',
                'verbose_name_plural': 'Blocked IPs',
                'ordering': ('-date_updated',),
                'db_table': 'redirect_Blocked',
            },
        ),
        migrations.CreateModel(
            name='ClickLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('referer', models.CharField(max_length=512, null=True)),
                ('user_agent', models.CharField(max_length=1024, null=True)),
                ('ip_addr', models.GenericIPAddressField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Click',
                'verbose_name_plural': 'Clicks',
                'ordering': ('-date_created',),
                'db_table': 'redirect_Click',
            },
        ),
        migrations.CreateModel(
            name='SiteLink',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('link', models.URLField(max_length=512)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=512, unique=True)),
                ('note', models.TextField(blank=True, verbose_name='body')),
                ('note_html', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
                'ordering': ('-date_created',),
                'db_table': 'redirect_Link',
            },
        ),
        migrations.AddField(
            model_name='clicklink',
            name='link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='redirection.SiteLink'),
        ),
    ]