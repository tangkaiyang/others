# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 6:29
# @Author   : tangky
# @Site     : 
# @File     : xml_test.py
# @Software : PyCharm

# from lxml import etree
# text = '''
# <div>
# <ul>
# <li class="item-0"><a href="link1.html">first item</a></li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-inactive"><a href="link3.html">third item</a></li>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a>
# </ul>
# </div>
# '''
# html = etree.HTML(text) # 调用HTML类进行初始化,构造一个XPath解析对象.etree可以自动修正HTML文本
# print(type(html))
# result = etree.tostring(html) # 输出修正后的HTML代码,结果为bytes类型
# print(type(result))
# print(result.decode('utf-8')) # decode方法将bytes解码为string
# 补全了li节点标签,自动添加了body,html节点
# 直接读取文本解析
# from lxml import etree
# html = etree.parse('D:\PycharmProjects\others\网络爬虫开发实战\chapter03\zhihu.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8')) # 多了DOCTYPE声明
# 5.所有节点
# 一般会用//开头的XPath规则来选取所有符合要求的节点.
# 选取所有节点//*
# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//*')
# print(result) # 每个元素是Element类型,其后跟了节点的名称
# 获取li节点
# result = html.xpath('//li')
# print(result)
# print(result[0])
# 6.子节点
# 通过/或//即可查找元素的子节点或子孙节点.
# //li/a
# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a')
# result1 = html.xpath('//li//a')
# print(result == result1)
# 7.父节点
# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class') # 也可以通过parent::获取父节点
# print(result)
# 8.属性匹配:用@符号进行属性过滤
# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-1"]') # 选区class为item-1的li节点
# print(result)
# 9.文本获取:text()方法获取节点中的文本
# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/text()')
# result = html.xpath('//li[@class="item-0"]//text()') # //选取子孙节点,会多出/r/n(li节点内部的文本)
# result = html.xpath('//li[@class="item-0"]/a/text()') # 选取到a节点
# result = etree.tostring(html)
# print(result)
"""没有获取到任何文本,只获取到了一个/r/n:
因为XPath中text()前面是/,而此处/的含义是选取直接子节点,li的直接子节点是a节点,文本都是在a节点内部的,所有
这里匹配到的结果就是被修正的li节点内部的换行符,因为自动修正的li节点的尾标签换行了"""
# 10.属性获取,@符号获取
# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result) # 返回一个列表
# 11.属性多值匹配:某些节点的某个属性可能有多个值,需要contains()函数
from lxml import etree
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
# result = html.xpath('//li[@class="li li-first"]/a/text()')
result = html.xpath('//li[contains(@class="li")]/a/text()')
print(result)