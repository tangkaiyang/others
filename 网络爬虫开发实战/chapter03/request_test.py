# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/19 7:45
# @Author   : tangky
# @Site     : 
# @File     : request_test.py
# @Software : PyCharm

from urllib.request import Request, urlopen
request = Request('https://python.org')
response = urlopen(request)
print(response.read().decode('utf-8'))