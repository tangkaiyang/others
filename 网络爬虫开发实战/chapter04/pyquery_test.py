# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 15:31
# @Author   : tangky
# @Site     : 
# @File     : pyquery_test.py
# @Software : PyCharm

# 初始化
# # 字符串初始化
# html = '''
# <div id="container">
# <ul class="list">
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html) # 初始化
# print(doc('li')) # 初始化对象传入CSS选择器
# # URL初始化:PyQuery对象首先请求这个URL,然后用得到的HTML内容完成初始化
# from pyquery import PyQuery as pq
# doc = pq(url='https://cuiqingcai.com')
# print(doc('title'))
# # 文件初始化:传递本地的文件名,参数指定为filename即可
# from pyquery import PyQuery as pq
# doc = pq(filename='./test.html')
# print(doc('li'))
# 3.基本CSS选择器
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('#container .list li')) # 先选取id为container的节点,然后选取其内部的class为list的节点内部的所有li节点.
# print(type(doc('#container .list li'))) # 类型依然是PyQuery类型
# 4.查找节点
# # 子节点:find()方法,传入的参数是CSS选择器
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# lis = items.find('li') # find()的查找范围是节点的所有子孙节点
# lis = items.children('li') # children()查找范围是节点的所有子节点
# lis = items.children('.active') # 筛选子节点中class为active的节点
# lis = doc.children('li') # children()查找范围是节点的所有子节点
# lis = doc.find('li')
# print(type(lis))
# print(lis)
# # 父节点:parent()方法获取某个节点的直接父节点,parents()方法返回所有祖先节点,传入CSS选择器,筛选祖先节点
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
# class="item-0 active"代表有两个class
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# container = items.parent()
# print(type(container)) # 依然是PyQuery类型
# print(container)
# items = doc('.item-0')
# parents = items.parents()
# parents = items.parents('.wrap') # 传入CSS选择器,筛选祖先节点
# print(type(parents))
# print(parents)
# # 兄弟节点:siblings()方法
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.list .item-0.active') # 选择class为list的节点内部class为item-0和active的节点,
# print(li.siblings())
# print(li.siblings('.active')) # 向siblings()传入CSS选择器,筛选兄弟节点
# 5.遍历:pyquery的选择结果可能是多个节点,也可能是单个节点,类型都是PyQuery类型,并没有返回像Beautiful Soup那样的列表
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li) # 直接输出
# print(str(li)) # 直接转成字符串
# lis = doc('li').items() # 调用items()方法遍历li节点
# print(type(lis)) # 生成器
# for li in lis:
#     print(li, type(li)) # PyQuery类型
# 6.获取信息:提取节点所包含的信息,属性,文本等
# # 获取属性:提取到某个PyQuery类型的节点后,就可以调用attr()方法来获取属性
from pyquery import PyQuery as pq
doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a)) # PyQuery类型
# print(a.attr('href')) # 调用attr()方法,传入属性的名称
# print(a.attr.href) # 通过调用attr属性来获取属性
# a = doc('a') # 选中多个元素,返回第一个节点的属性
# print(a, type(a))
# print(a.attr('href'))
# print(a.attr.href)
# 遍历获取多个节点的属性
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))
# # 获取文本