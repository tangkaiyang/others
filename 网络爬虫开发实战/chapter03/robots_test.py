# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 19:41
# @Author   : tangky
# @Site     : 
# @File     : robots_test.py
# @Software : PyCharm

from urllib.robotparser import RobotFileParser

# rp = RobotFileParser()
# rp.set_url('http://jianshu.com/robots.txt')
# fp = rp.read()
# print(fp)
# print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d')) # 第一个参数是User-agent,第二个是要抓取的URL
# print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=18&type=collections'))

# 同样可以使用parse()方法执行读取和分析:parse用来解析robots.txt文件,传入的参数是robots.txt某些行的内容,会按照robots.txt的语法规则来分析这些内容
from urllib.request import urlopen, Request
rep = Request(url='http://www.jianshu.com/robots.txt', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'})
rp = RobotFileParser()
rp.parse(urlopen(rep).read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'https://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'https://www.jianshu.com/search?q=python&page=18&type=collections'))
# response = urlopen('http://www.jianshu.com/robots.txt')