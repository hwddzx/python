# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-24 17:32
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0004_auto_20190123_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodityclassmodel',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='activityzonemodel',
            name='is_on_sale',
            field=models.BooleanField(default=False, verbose_name='是否上线'),
        ),
        migrations.AlterField(
            model_name='commodityspumodel',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='详情'),
        ),
    ]
