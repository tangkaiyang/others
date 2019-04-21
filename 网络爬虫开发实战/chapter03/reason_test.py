# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 14:12
# @Author   : tangky
# @Site     : 
# @File     : reason_test.py
# @Software : PyCharm

# from urllib import request, error
#
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# # except error.URLError as e:
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n') # 捕获了HTTPError异常,输出了reason,code,headers属性
#
# # 由于HTTPError是URLError的子类,所以可以先选择捕获子类的错误,再去捕获父类的错误
# from urllib import request, error
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.hm')
# except error.HTTPerror as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

import socket, urllib.request, urllib.error
try:
    response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    print(e.reason)
    print(type(e.reason)) # reason属性的结果是socket.timeout类,所以,这里我们可以用isinstance()方法来判断它的类型,
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
