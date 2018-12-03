# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import re
import time


import requests
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse

from lukMsg.models import LukInfo, LukUser

@login_required
def lukTotalMsg(req):
    url = 'https://www.f2pool.com/xmr/4DSQMNzzq46N1z2pZWAVdeA6JvUL9TCB2bnBiA3ZzoqEdYJnMydt5akCa3vtmapeDsbVKGPFdNkzqTcJS8M8oyK7WGitvMmKXCHMHeYdRt'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.79 Safari/537.36'
    }
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = requests.get(url, headers=header, verify=False, timeout=10)
    response.encoding = 'utf-8'
    html_data = response.text
    soup = BeautifulSoup(html_data, "html.parser")
    income_list = soup.find_all('span', class_="item-value")
    xmr_imcome = []
    for i in income_list:
        xmr_imcome.append(i.get_text())
    lukuser_online = soup.find('span', class_="item-online-value").get_text()
    lukuser_all = soup.find('span', class_="item-all-value").get_text()
    xmr_row = soup.find_all('strong')
    xmr_run = []
    for row in xmr_row:
        xmr_run.append(row.get_text())
    table = soup.find('table', id="workers")
    td_compile = re.compile(r"<td>(.*)</td>", re.I)
    td = td_compile.findall(str(table))
    list, td_dict, num = [], {}, 0
    td_list = []
    for each in td:
        if num < 4:
            td_list.append(each)
            num += 1
        else:
            td_dict['mac'] = td_list[0]
            td_dict['fifteen'] = td_list[1]
            td_dict['tweentyfour'] = td_list[2]
            td_dict['reject'] = td_list[3]
            time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(re.sub(r'\D', '', each)[:10])))
            td_dict['time'] = time1
            list.append(td_dict)
            td_list, td_dict = [], {}
            num = 0
    return render(req, 'lukTotalMsg.html', {'xmr_imcome': xmr_imcome, 'lukuser_online': lukuser_online,
                                      'lukuser_all': lukuser_all, 'xmr_run': xmr_run, 'list': list})

@login_required
def index(req):
    totalNum = LukInfo.objects.all().count()
    runNum = LukInfo.objects.filter(serverStat='True').count()
    stopNum = LukInfo.objects.filter(serverStat='Flase').count()
    offNum = LukInfo.objects.filter(mechineStat='Flase').count()
    return render(req, 'index.html', {'totalNum': totalNum, 'runNum': runNum,
                                            'stopNum': stopNum, 'offNum': offNum})

@login_required
def lukUser(req):
    return render(req, 'lukuser.html')

@login_required
def lukService(req):
    global searchName, searchStat
    searchName = req.GET.get("name")
    searchStat = req.GET.get("state")
    return render(req, 'lukservice.html')

@login_required
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
    lenth = host.count()
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
    lenth = host.count()
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
            if data. has_key("macAddr"):
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


def lukAddSn(req):
    if req.method == "POST":
        print "yes"
        luk_data = json.loads(req.body)
        for data in luk_data:
            if data. has_key("macAddr"):
                macAddr = data['macAddr']

                for addr in macAddr:
                    try:
                        lukinfo = LukInfo.objects.get(macAddr=addr)
                    except Exception:
                        lukinfo = LukInfo()
                    lukinfo.lukSn = data['sn']
                    lukinfo.macAddr = addr
                    lukinfo.save()

                # lukinfo.save()
        return HttpResponse()
    else:
        return HttpResponse("error")


def login_user(request):
    redirect_to = request.GET.get('next', '')
    if request.method == 'POST':
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        check = request.POST.get("check")
        next = request.GET.get("next")
        user = authenticate(username=username, password=passwd)
        if user:
            if user.is_active:
                if user.is_staff:
                    login(request, user)
                    if check:
                        request.session.set_expiry(None)
                    else:
                        request.session.set_expiry(0)
                    if next:
                        return HttpResponseRedirect(next)
                    else:
                        return redirect(reverse('index'))
                else:
                    if username != "admin":
                        return render(request, 'login.html', {'error': u'用户没有登入权限!'})
            else:
                return render(request, 'login.html', {'error': u'用户没有激活!'})
        else:
            return render(request, 'login.html', {'error': u'用户名或密码错误!'})
    return render(request, 'login.html', {'redirect_to': redirect_to})


def logout_user(req):
    logout(req)
    return redirect(reverse('login'))