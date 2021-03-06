# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-03 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LukInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macAddr', models.CharField(max_length=255, unique=True, verbose_name='MAC\u5730\u5740')),
                ('serverStat', models.CharField(blank=True, max_length=255, verbose_name='\u670d\u52a1\u72b6\u6001')),
                ('mechineStat', models.CharField(blank=True, max_length=255, verbose_name='\u673a\u5668\u72b6\u6001')),
                ('mechineSensor', models.CharField(blank=True, max_length=255, verbose_name='\u673a\u5668\u6e29\u5ea6')),
                ('ipAddr', models.CharField(blank=True, max_length=255, verbose_name='IP\u5730\u5740')),
                ('username', models.CharField(blank=True, max_length=255, verbose_name='\u7528\u6237\u540d\u79f0')),
                ('runTime', models.CharField(blank=True, max_length=255, verbose_name='\u63d0\u4ea4\u65f6\u95f4')),
                ('lukSn', models.CharField(blank=True, default='-', max_length=255, verbose_name='\u77ff\u673a\u5e8f\u53f7')),
            ],
        ),
        migrations.CreateModel(
            name='LukUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
            ],
        ),
    ]
