# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LukInfo(models.Model):
    macAddr = models.CharField('MAC地址', max_length=255)
    serverStat = models.CharField('服务状态', max_length=255)
    mechineStat = models.CharField('机器状态', max_length=255)
    mechineSensor = models.CharField('机器温度', max_length=255)
    ipAddr = models.CharField('IP地址', max_length=255)
    username = models.CharField('用户名称', max_length=255)
    runTime = models.CharField('运行时间', max_length=255)


class LukUser(models.Model):
    user = models.CharField(max_length=255)
    user_id = models.IntegerField(unique=True)
