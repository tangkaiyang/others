# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/19 7:45
# @Author   : tangky
# @Site     : 
# @File     : request_test.py
# @Software : PyCharm

# from urllib.request import Request, urlopen
# request = Request('https://python.org')
# response = urlopen(request)
# print(response.read().decode('utf-8'))

from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))