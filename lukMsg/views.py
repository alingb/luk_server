# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import time

from django.forms import model_to_dict
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
from lukMsg.models import LukInfo, LukUser


def index(req):
    return render(req, 'starter.html')


def lukTotalMsg(req):
    totalNum = len(LukInfo.objects.all())
    runNum = len(LukInfo.objects.filter(serverStat='True'))
    stopNum = len(LukInfo.objects.filter(serverStat='Flase'))
    offNum = len(LukInfo.objects.filter(mechineStat='Flase'))
    return render(req, 'luktotalmsg.html', {'totalNum': totalNum, 'runNum': runNum,
                                            'stopNum': stopNum, 'offNum': offNum})


def lukUser(req):
    return render(req, 'lukuser.html')


def lukService(req):
    searchName = req.GET.get("name")
    searchStat = req.GET.get("state")
    if searchName and searchStat:
        global searchName, searchStat
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
    if searchName and searchStat:
        if searchName == "serverStat":
            host = LukInfo.objects.filter(serverStat=searchStat)
        elif searchName == "mechineStat":
            host = LukInfo.objects.filter(mechineStat=searchStat)
    else:
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


def lukAddMsg(req):
    import time
    if req.method == 'POST':
        luk_data = json.loads(req.body)
        for data in luk_data:
            if data.has_key("macAddr"):
                macAddr = data['macAddr']
                try:
                    lukinfo = LukInfo.objects.get(macAddr=macAddr)
                except Exception:
                    lukinfo = LukInfo()
                lukinfo.macAddr = data['macAddr']
                lukinfo.mechineSensor = data['mechineSensor']
                lukinfo.mechineStat = data['mechineStat']
                lukinfo.serverStat = data['serverStat']
                lukinfo.ipAddr = data['ipAddr']
                lukinfo.runTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                lukinfo.save()
            else:
                ipAddr = data["ipAddr"]
                try:
                    lukinfo = LukInfo.objects.get(ipAddr=ipAddr)
                except Exception:
                    lukinfo = LukInfo()
                lukinfo.mechineSensor = data['mechineSensor']
                lukinfo.mechineStat = data['mechineStat']
                lukinfo.serverStat = data['serverStat']
                lukinfo.ipAddr = data['ipAddr']
                lukinfo.runTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                lukinfo.save()
        return HttpResponse('ok')
    else:
        return HttpResponse('off')

