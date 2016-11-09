# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0004_auto_20161105_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crawl2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('websites', models.ManyToManyField(related_name='websites2', to='websites.Website')),
            ],
        ),
    ]