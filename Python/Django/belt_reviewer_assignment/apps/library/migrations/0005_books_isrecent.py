# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20170222_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='isRecent',
            field=models.BooleanField(default=False),
        ),
    ]
