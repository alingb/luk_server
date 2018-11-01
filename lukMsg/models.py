# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LukInfo(models.Model):
    macAddr = models.CharField('MAC地址', max_length=255, unique=True)
    serverStat = models.CharField('服务状态', max_length=255, blank=True)
    mechineStat = models.CharField('机器状态', max_length=255, blank=True)
    mechineSensor = models.CharField('机器温度', max_length=255, blank=True)
    ipAddr = models.CharField('IP地址', max_length=255, blank=True)
    username = models.CharField('用户名称', max_length=255, blank=True)
    runTime = models.CharField('提交时间', max_length=255, blank=True)
    lukSn = models.CharField('矿机序号', max_length=255, blank=True, default='-')


class LukUser(models.Model):
    user = models.CharField(max_length=255)
    def __unicode__(self):
        return self.user
