# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 14:46
# @Author   : tangky
# @Site     : 
# @File     : urlunparse_test.py
# @Software : PyCharm

from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))