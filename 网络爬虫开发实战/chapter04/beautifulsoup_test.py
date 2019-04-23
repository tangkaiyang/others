# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 10:33
# @Author   : tangky
# @Site     : 
# @File     : beautifulsoup_test.py
# @Software : PyCharm

from bs4 import BeautifulSoup

# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.p.string)
# print(soup)
# 4.基本用法
# html = '''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# '''
# soup = BeautifulSoup(html, 'lxml') # BeautifulSoup对象,第二个参数是解析器的类型,自动修正不标准的html
# print(soup.prettify()) # 把要解析的字符串以标准的缩进格式输出,
# print(soup.title.string) #输出title节点的文本内容
# 5.节点选择器:直接调用节点的名称就可以选择节点元素,在调用string属性就可以获得节点内的文本了
# 选择元素
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p) # 只选择到第一个匹配的节点,后面的会忽略
# 提取信息
# 1)获取名称:name属性
# print(soup.title.name)
# 2)获取属性:每个节点可能有多个属性,比如id和class等,选择这个节点元素后,可以调用attrs获取所有属性
# print(soup.p.attrs)
# print(soup.p)
# print(soup.p['name'])
# print(soup.p['class'])
# 注意:有的返回字符串,有的返回字符串组成的列表,name属性是唯一的,而class一个节点元素可能有多个class,返回列表
# 3)获取内容:利用string属性获取节点元素包含的文本内容
# print(soup.p.string)
# 嵌套选择
# print(type(soup.p)) # 返回的是bs4.element.Tag类型,可以继续调用节点进行下一步的选择
# html = '''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.head)
# print(type(soup.head))
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)
# 关联选择:有时候不能做到一步就选到想要的节点元素,需要先选中某一个节点元素,然后以他为基准再选择它的子节点,父节点,兄弟节点等
# 1)子节点和子孙节点:
# 选取节点元素之后,如果想要获取它的直接子节点,可以调用contents属性
# html = '''
# <html>
# <head>
# <title>The Dormouse's story</title>
# </head>
# <body>
# <p class="story">
#     Once upon a time there were three little sisters; and their names were
#     <a href="http://example.com/elsie" class="sister" id="link1">
# <span>Elsie</span>
# </a>
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
# and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
# and they lived at the bottom of a well.
# </p>
# <p class="story">...</p>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.contents) # 返回结果是列表形式.p节点里既包含文本,又包含节点,最后会将他们以列表形式统一返回
# 注意:列表中的每个元素都是p节点的直接子节点
# for content in soup.p.contents:
#     print(repr(content))
# 调用children属性得到相应的结果
# print(soup.p.children) # 返回迭代器类型
# for i, child in enumerate(soup.p.children):
#     print(i, child)
# 得到所有的子孙节点,调用descendants属性:
# print(soup.p.descendants) # 返回生成器对象,递归查询所有子节点,得到所有的子孙节点
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)
# 2)父节点和祖先节点:获取某个节点元素的父节点,可以调用parent属性
# html = """
# <html>
# <head>
# <title>The Dormouse's story</title>
# </head>
# <body>
# <p class="story">
#             Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">
# <span>Elsie</span>
# </a>
# </p>
# <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.a.parent) # 输出父节点p节点及其全部的内容
# 输出的仅仅是a节点的直接父节点,而没有再向外寻找父节点的祖先节点
# 要获取所有的祖先借点调用parents属性
# print(soup.a.parents) # 生成器对象
# for i, child in enumerate(soup.a.parents):
#     print(i, child) # 输出祖先节点及其全部的内容
# 3)兄弟节点:next_sibling:获取节点的下一个兄弟元素,previous_sibling获取节点的上一个兄弟元素,
# next_siblings返回所有前面的兄弟节点的生成器,previous_siblings获取所以后面的兄弟节点的生成器
# html = """
# <html>
# <body>
# <p class="story">
#             Once upon a time were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">
# <span>Elsie</span>
# </a>
#             Hello
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
# </p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print('Next Sibling', soup.a.next_sibling)
# print('Prev Sibling', soup.a.previous_sibling)
# print('Next Siblings', soup.a.next_siblings)
# print(list(soup.a.next_siblings))
# print('Prev Siblings', soup.a.previous_siblings)
# print(list(soup.a.previous_siblings))
# 4)提取信息:提取关联元素节点的信息,如文本,属性
# html = """
# <html>
# <body>
# <p class="story">
#             Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie"
# class="sister" id="link2">Lacie</a>
# </p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print('Next Sibling:')
# print(type(soup.a.next_sibling))
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.string)
# print('Parent:')
# print(type(soup.a.parents))
# print(type(list(soup.a.parents)[0]))
# print(list(soup.a.parents)[0])
# print(list(soup.a.parents)[0].attrs['class'])
# 6.方法选择器
# find_all(name, attrs, recursive, text, **kwargs),查询所有符合条件的元素
# name节点名<li>节点名为li,attrs属性(字典),text匹配节点的文本(字符串或正则表达式)
html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0])) # 都是Tag类型,可以进行嵌套查询
# for ul in soup.find_all(name='ul'): # 遍历每个ul标签
#     print(ul.find_all(name='li'))
# for li in soup.find_all(name='li'):
#     print(li.string) # 返回文本
#     print(li.attrs['class'])
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))
# print(soup.find_all(id='list-1'))
# print(soup.find_all(text='Foo'))
# import re
# print(soup.find_all(text=re.compile('a')))
# find():返回单个元素,第一个匹配的元素
# 方法与find_all()和find()完全相同,查询范围不同
# # find_parents()和find_parent():前者返回所有祖先节点,后者返回直接父节点
# # find_next_siblings()和find_next_sibling():前者返回后面所有的兄弟节点,后者返回后面第一个兄弟节点
# # find_previous_siblings()和find_previous_sibling():前者返回前面所有兄弟节点,后者返回前面第一个兄弟节点
# # find_all_next()和find_next():前者返回节点后所有符合条件的节点,后者返回第一个符合条件的节点
# # find_all_previous()和find_previous():前者返回节点前所有符合条件的节点,后者返回节点前第一个符合条件的节点
# 7.CSS选择器
# 调用select()方法,传入相应的CSS选择器
html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li')) # 所有ul节点下面的所有li节点,结果便是所有li节点组成的列表
# print(soup.select('#list-2 .element'))
# print(type(soup.select('ul')[0])) # 类型依然是Tag类型
# # 嵌套选择:select()方法同样支持嵌套选择.
# 先选择所有ul节点,再遍历每个ul节点,选择其li节点
# for ul in soup.select('ul'):
#     print(ul.select('li'))
# # 获取属性:节点类型还是Tag类型,所以获取属性还可以用原来的方法.
# for ul in soup.select('ul'):
#     print(ul['id']) # 直接传入中括号和属性名
#     print(ul.attrs['id']) # 通过attrs(字典)属性获取属性值
# # 获取文本:除了string属性,还有get_text()方法
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)
