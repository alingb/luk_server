# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.forms import model_to_dict
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
from lukMsg.models import LukInfo, LukUser


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


def lukAddUser(req):
    if req.method == 'POST':
        info = req.POST.get('data')
        user = eval(info)['user']
        try:
            lukuser = LukInfo.objects.get(user=user)
        except:
            lukuser = LukUser()
        lukuser.user = user
        lukuser.save()
        return HttpResponse('ok')
    else:
        data = LukInfo.objects.all()
        return HttpResponse(data)


def lukUserChange(req):
    pass


def lukServerMsg(request):
    limit = request.GET.get("limit")
    offset = request.GET.get("offset")
    host = LukUser.objects.all()
    lenth = len(host)
    if not offset or not limit:
        host = host
    else:
        offset = int(offset)
        limit = int(limit)
        host = host[offset:offset + limit]
    data = []
    for each in host:
        data.append(model_to_dict(each))
    return HttpResponse(json.dumps({"rows": data, "total": lenth}))


def lukServiceMsg(request):
    limit = request.GET.get("limit")
    offset = request.GET.get("offset")
    host = LukInfo.objects.all()
    lenth = len(host)
    if not offset or not limit:
        host = host
    else:
        offset = int(offset)
        limit = int(limit)
        host = host[offset:offset + limit]
    data = []
    for each in host:
        data.append(model_to_dict(each))
    return HttpResponse(json.dumps({"rows": data, "total": lenth}))