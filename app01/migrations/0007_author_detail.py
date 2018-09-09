# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-09-09 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_authordetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='detail',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='app01.AuthorDetail'),
            preserve_default=False,
        ),
    ]