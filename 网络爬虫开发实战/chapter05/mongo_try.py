# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/24 8:16
# @Author   : tangky
# @Site     : 
# @File     : mongo_try.py
# @Software : PyCharm

import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
print(type(client))