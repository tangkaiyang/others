# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 14:51
# @Author   : tangky
# @Site     : 
# @File     : urlsplit_test.py.py
# @Software : PyCharm

from urllib.parse import urlsplit
result = urlsplit('http://www.baidu.com/index.html;user?id=6#comment')
print(result)
print(result[0], result.scheme, result[1], result.netloc, sep='\n')
