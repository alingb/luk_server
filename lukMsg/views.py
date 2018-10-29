# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req, 'starter.html')


def lukTotalMsg(req):
    return render(req, 'luktotalmsg.html')


def lukUser(req):
    return render(req, 'lukuser.html')


def lukService(req):
    return render(req, 'lukservice.html')


def lukSensor(req):
    return render(req, 'lukSensor.html')