# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 15:06
# @Author   : tangky
# @Site     : 
# @File     : urlencode_test.py
# @Software : PyCharm

from urllib.parse import urlencode

params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)