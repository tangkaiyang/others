# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 14:30
# @Author   : tangky
# @Site     : 
# @File     : urlparse_test.py
# @Software : PyCharm

from urllib.parse import urlparse

# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https') # 设定scheme参数,默认协议
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https') # 未设定协议类型时生效
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https', allow_fragments=False) # 忽略锚点
print(result.scheme, result[0], result.netloc, result[1], sep='\n')
print(type(result), result, sep='\n')