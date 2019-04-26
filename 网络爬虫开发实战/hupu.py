# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/26 14:45
# @Author   : tangky
# @Site     : 
# @File     : hupu.py
# @Software : PyCharm


import requests

response = requests.get('https://nba.hupu.com', verify=False)
with open('hupu.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
print(response.text)