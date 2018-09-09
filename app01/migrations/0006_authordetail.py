# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-09-09 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(default='SH', max_length=128)),
                ('language', models.CharField(default='Python', max_length=64)),
            ],
        ),
    ]
