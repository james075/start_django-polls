# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='comments',
            field=models.TextField(default=''),
        ),
    ]
