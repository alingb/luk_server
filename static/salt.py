#!/usr/bin/python
# _*_encoding:utf-8_*_
"""
# @TIME:2018/12/1 11:47
# @FILE:salt.py
# @Author:ytym00
"""

import json
import requests

import sys


def file_msg(fd):
    with open(fd, 'r') as fmsg:
        file_msg = fmsg.read()
    return file_msg


def data_parse(data):
    if data:
        data_list = []
        for each in data.split('\n'):
            each = each.split()
            data_dict = {"sn": each[0], "macAddr": [each[3], each[1], each[2]]}
            data_list.append(data_dict)
        return data_list
    else:
        return None


if __name__ == '__main__':
    fname = sys.argv[1]
    fmsg = file_msg(fname)
    data = data_parse(fmsg)
    data = json.dumps(data)
    a = requests.post('http://127.0.0.1:8080/lukServer/lukAddSn', data)
    print a.status_code
