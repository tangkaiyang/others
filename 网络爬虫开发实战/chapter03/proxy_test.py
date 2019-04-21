# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 13:48
# @Author   : tangky
# @Site     : 
# @File     : proxy_test.py
# @Software : PyCharm

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743', # 使用了ProxyHandler,其参数是一个字典,键名是协议类型(如HTTP或HTTPS等),键值是代理链接,可以添加多个代理
    'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler) # 然后利用这个Handler及build_opener()方法构造一个Opener,之后发送请求即可
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().encode('utf-8'))
except URLError as e:
    print(e.reason)