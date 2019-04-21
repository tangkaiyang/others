# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 20:29
# @Author   : tangky
# @Site     : 
# @File     : requests_test.py
# @Software : PyCharm

# import requests

# requests中相应的get()方法就是urllib库中的urlopen()方法
# r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# r = requests.get('http://httpbin.org/get')
# r = requests.get('http://httpbin.org/get?name=germey&age=22')
# print(r.text)
# data = {'name': 'germey', 'age': '22'}
# r = requests.get('http://httpbin.org/get', params=data)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))
# print(r.text)

# 网页返回类型为str类型,是JSON格式的,想直接解析返回结果,得到一个字典格式,调用json()方法
# 如果返回不是JSON类型,便会出现解析错误,抛出json.decoder.JSONDecodeError异常

# 抓取网页
# import requests
# import re
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# print(r.text)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S) # .匹配/n之外任何单字符,re.S(DOTALL)'.'任意匹配模式
# titles = re.findall(pattern, r.text)
# print(titles)

# 抓取二进制数据
# GitHub站点图标
import requests
r = requests.get('https://zhihu.com/favicom.ico')
print(r.text)
print(r.content)