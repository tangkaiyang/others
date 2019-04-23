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
# html = '''
# <div class="wrap">
# <div id="container">
# <ul class="list">
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# </div>
# '''
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
# from pyquery import PyQuery as pq
# doc = pq(html)
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
# # 获取文本:调用text()方法,获取内部的文本信息,会忽略掉节点内部包含的所有HTML,只返回纯文字内容
# a = doc('.item-0.active a')
# print(a)
# print(a.text())
# print(a.html()) # 获取这个节点内部的HTML文本
# li = doc('li') # 同时选中多个节点
# print(li.html()) # html()方法返回第一个li节点的内部HTML文本,获取多个需要遍历
# print(li.text()) # text()方法返回了所有的li节点内部的纯文本,中间用一个空格分隔开,即返回结果是一个字符串
# print(type(li.text()))
# 7.节点操作:pyquery提供了一些类方法来对节点进行动态修改,比如为某个节点添加一个class,移除某个节点等,这些操作有时候会为提取信息带来极大的便利
# # add_class和remove_class动态改变节点的class属性
# html = '''
# <div class="wrap">
# <div id="container">
# <ul class="list">
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# # li.remove_class('active')
# li.remove_class('active')
# print(li)
# li.add_class('active')
# print(li)
# # attr,text和html
# li = doc('.item-0.active')
# print(li)
# print(li.attr('class')) # attr(key)获得key对应的属性值
# li.attr('name', 'link') # attr(key, value)如果key不存在,添加key=value到属性
# print(li)
# li.attr('class', 'item-0') # key存在则修改当前属性值
# print(li)
# li.text('changed item') # 不传参数,获取节点内纯文本内容,传入参数则修改
# print(li)
# li.html('<span>changed item</span>') # 获取节点内HTML文本,如果传入参数,进行赋值
# print(li)
# # remove():移除,有时会为信息的提取带来极大的便利
# html = '''
# <div class="wrap">
#     Hello, World
# <p>This is a paragraph.</p>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())
# wrap.find('p').remove()
# print(wrap.text())
# # 还有很多节点操作的方法,如append(),empty()和prepend(),和jQuery用法完全一致
# 8.伪类选择器,例如选择第一个节点,最后一个节点,奇偶数节点,包含某一文本的节点等
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
from pyquery import PyQuery as pq

doc = pq(html)
li = doc('li:first-child')  # 第一个li节点
print(li)
li = doc('li:last-child')  # 最后一个li节点
print(li)
li = doc('li:nth-child(2)')  # 第二个li节点
print(li)
li = doc('li:gt(2)')  # 第三个li之后的li节点
print(li)
li = doc('li:nth-child(2n)')  # 偶数位置的li节点
print(li)
li = doc('li:contains(second)')  # 包括second文本的li节点
print(li)
