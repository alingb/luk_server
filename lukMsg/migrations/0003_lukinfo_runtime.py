# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-28 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lukMsg', '0002_auto_20181028_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='lukinfo',
            name='runTime',
            field=models.CharField(default='', max_length=255, verbose_name='\u8fd0\u884c\u65f6\u95f4'),
            preserve_default=False,
        ),
    ]
