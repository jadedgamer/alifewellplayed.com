# Generated by Django 2.0 on 2018-04-22 16:53

import django.contrib.sites.models
from django.db import migrations, models
import django.db.models.deletion
import replica.pulse.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('pulse', '0005_auto_20180422_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('icon', models.SlugField(blank=True, choices=[('fa fa-home', 'Home'), ('fa fa-pencil-square-o', 'Posts'), ('fa fa-book', 'Notes'), ('fa fa-tags', 'Topics'), ('fa fa-code-fork', 'Channels'), ('fa fa-file-image-o', 'Media'), ('fa fa-cogs', 'Gears')], max_length=510)),
                ('title', models.CharField(default='Untitled', max_length=510)),
                ('description', models.CharField(blank=True, help_text='Optional subtitle', max_length=510)),
                ('slug', models.SlugField(blank=True, max_length=510)),
                ('url', models.CharField(blank=True, max_length=510)),
                ('weight', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(blank=True, default=replica.pulse.models.DefaultEntry, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='pulse.Entry')),
            ],
            options={
                'verbose_name': 'Menu Item',
                'verbose_name_plural': 'Menu Items',
                'db_table': 'r_MenuItem',
                'ordering': ('weight',),
            },
        ),
        migrations.CreateModel(
            name='MenuPosition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Untitled', max_length=510)),
                ('slug', models.SlugField(max_length=510)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
                'db_table': 'r_MenuPosition',
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=510)),
                ('slug', models.SlugField(max_length=510)),
                ('author', models.CharField(blank=True, max_length=510)),
                ('is_enabled', models.BooleanField(choices=[(True, 'Enabled'), (False, 'Disabled')], default=True, help_text='Check to enable plugin')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Plugin',
                'verbose_name_plural': 'Plugins',
                'db_table': 'r_Plugin',
                'ordering': ('slug', 'date_updated'),
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('site_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sites.Site')),
                ('is_enabled', models.BooleanField(choices=[(True, 'Enabled'), (False, 'Disabled')], default=True, help_text='Is site enabled?')),
                ('password', models.CharField(blank=True, max_length=128)),
                ('secret_token', models.CharField(blank=True, max_length=12)),
                ('view_settings', models.TextField(default='{}')),
                ('author', models.CharField(blank=True, max_length=510)),
                ('description', models.TextField(blank=True, help_text='Site Description', null=True)),
                ('summary', models.TextField(blank=True, help_text='Summary')),
                ('summary_html', models.TextField(blank=True, editable=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('featured', models.ForeignKey(blank=True, help_text='Featured Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured', to='pulse.Media')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo', to='pulse.Media')),
            ],
            options={
                'verbose_name': 'Site Settings',
                'verbose_name_plural': 'Site Settings',
                'db_table': 'r_SiteSettings',
            },
            bases=('sites.site',),
            managers=[
                ('objects', django.contrib.sites.models.SiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='menuitem',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.MenuPosition'),
        ),
    ]