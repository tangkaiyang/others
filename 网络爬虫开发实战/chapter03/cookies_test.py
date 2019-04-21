# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 13:53
# @Author   : tangky
# @Site     : 
# @File     : cookies_test.py
# @Software : PyCharm

import urllib.request, http.cookiejar

cookie = http.cookiejar.CookieJar() # 首先必须声明一个CookieJar对象.
handler = urllib.request.HTTPCookieProcessor(cookie) # 利用HTTPCookieProcessor构建一个Handler,
opener = urllib.request.build_opener(handler) # 利用build_opener()方法构建出Opener,执行open()函数即可
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value) # 输出每条Cookie的名称和值

# 输出为文件格式
# filename = 'cookies1.txt'
# # cookie = http.cookiejar.MozillaCookieJar(filename) # CookieJar需要换成MozillaCookieJar,在生成文件时需要,是CookieJar的子类,可以用来处理Cookies和文件相关的事件,比如读取和保存Cookies,可以将Cookies保存成Mozilla型浏览器的Cookies格式
# cookie = http.cookiejar.LWPCookieJar(filename)# LWPCookieJar同样可以读取和保存Cookies,但是保存的格式和MozillaCookieJar不一样,保存成libwww-perl(LWP)格式的Cookies文件
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# 读取并利用Cookies文件
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies1.txt', ignore_expires=True, ignore_discard=True) # 调用load()方法读取本地Cookies文件
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))