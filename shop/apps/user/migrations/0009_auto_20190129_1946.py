# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-29 19:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_useraddress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': '用户表'},
        ),
    ]
