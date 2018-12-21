#!/usr/bin/python
# _*_encoding:utf-8_*_
"""
# @TIME: 2018/12/20 9:38
# @FILE: luk_info.py
# @Author: ytym00
"""
import json
import socket
from subprocess import PIPE, Popen

import re

import time

import requests


def command_exec(cmd):
    data = Popen(cmd, stdin=PIPE, stdout=PIPE, shell=True)
    cmd_info = data.stdout.read()
    return cmd_info


def searchInfo(msg):
    if msg:
        msg = msg.group(1)
    else:
        msg = None
    return msg


def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return {"ipAddr": ip}


def get_address_mac():
    net_info = command_exec("ip a")
    mac_compile = re.compile(r"link/ether\s([a-fA-F\d:]{17})\sbrd", re.M)
    mac = mac_compile.search(net_info)
    mac = searchInfo(mac)
    if mac:
        mac = mac.replace(":", "")
    return {"macAddr": mac}


def get_luk_sensor():
    sensor = command_exec("sensors")
    temp_compile = re.compile(r"Physical id 0:\s+\+(\d+(\.\d+)?).*?\s\(high.*", re.M)
    temp = temp_compile.search(sensor)
    temp = searchInfo(temp)
    return {"mechineSensor": temp}


def get_service_state():
    state = command_exec("systemctl status luk_phi")
    if "active" in state:
        return {"serverStat": True}
    else:
        return {"serverStat": False}


if __name__ == "__main__":
    send_dict = {}
    send_dict.update(get_host_ip())
    send_dict.update(get_address_mac())
    send_dict.update(get_luk_sensor())
    send_dict.update(get_service_state())
    send_dict.update({"mechineStat": True})
    send_dict.update({"runTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))})
    data = json.dumps(send_dict)
    url = "http://192.168.1.112/lukServer/lukAddMsg"
    a = requests.post(url, data)
    print(a.status_code)
