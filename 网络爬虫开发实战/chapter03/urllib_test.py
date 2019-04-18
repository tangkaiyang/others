# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/19 7:14
# @Author   : tangky
# @Site     : 
# @File     : urllib_test.py
# @Software : PyCharm

from urllib import request

# response = request.urlopen('https://nba.hupu.com/')
# print(response.read().decode('utf-8'))
# print(type(response))
# HTTPResponse对象,主要包含read(),readinto(),getheader(name),getheaders(),fileno()等方法,以及msg,version,status,reason,debuglevel,closed等属性
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# print(response.getheaders()[0][1])
from urllib import parse, error
import socket

data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
print(data)
try:
    response = request.urlopen('http://httpbin.org/post', data=data, timeout=0.1)
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
# print(response.read())
# print(response.read().decode('utf-8'))