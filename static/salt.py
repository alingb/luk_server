#!/usr/bin/python
# _*_encoding:utf-8_*_
"""
# @TIME:2018/12/1 11:47
# @FILE:salt.py
# @Author:ytym00
"""

import json
import requests

data = [{"sn": 123456, "macAddr": [23456, 23456, 34567]}, {"sn": 123457, "macAddr": [23457, 23457, 34568]}]
data = json.dumps(data)
a = requests.post('http://127.0.0.1:8080/lukServer/lukAddSn', data)
print a.text
