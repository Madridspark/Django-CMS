# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0028_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='heroimages',
            options={'verbose_name': '\u8f6e\u64ad\u56fe\u7247\u7684\u94fe\u63a5\u548c\u6587\u4ef6\u540d', 'verbose_name_plural': '\u8f6e\u64ad\u56fe\u7247'},
        ),
        migrations.AlterModelOptions(
            name='staticabout',
            options={'verbose_name': '\u5173\u4e8e\u672c\u7ad9', 'verbose_name_plural': '\u7f51\u7ad9\u7b80\u4ecb\u3001\u56e2\u961f\u6210\u5458\u4e0e\u8054\u7cfb\u65b9\u5f0f'},
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='theQRCode',
            field=models.FileField(default=0, upload_to='./central/logo-file/', verbose_name='\u4e8c\u7ef4\u7801'),
            preserve_default=False,
        ),
    ]