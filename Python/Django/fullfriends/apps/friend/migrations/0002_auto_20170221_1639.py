# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='friend2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friend.friend'),
        ),
    ]
