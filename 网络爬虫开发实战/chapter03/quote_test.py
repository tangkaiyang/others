# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 15:16
# @Author   : tangky
# @Site     : 
# @File     : quote_test.py
# @Software : PyCharm

from urllib.parse import quote, unquote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
print(unquote(url))