# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-18 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.IntegerField(default=1),
        ),
    ]
