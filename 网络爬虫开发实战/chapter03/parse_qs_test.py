# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 15:12
# @Author   : tangky
# @Site     : 
# @File     : parse_qs_test.py
# @Software : PyCharm

from urllib.parse import parse_qs

query = 'name=germey&age=22'
print(parse_qs(query))