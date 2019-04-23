# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 20:17
# @Author   : tangky
# @Site     : 
# @File     : json_test.py
# @Software : PyCharm

import json
# str = '''
# [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# }, {
#     "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# '''
# print(type(str))
# data = json.loads(str) # loads()方法将JSON文本字符串转换为JSON对象
# print(data)
# print(type(data))
# print(data[0]['name'])
# print(data[0].get('name'))
# print(data[0].get('age', 25)) # get传入第二个参数,'age'不存在是返回25
# print(data)
with open('./data.json', 'r', encoding='utf-8') as file:
    str = file.read()
    data = json.loads(str)
    # print(data)
# 3.输出JSON:利用dumps()方法将JSON对象转化为字符串
# with open('data1.json', 'w') as file:
#     file.write(json.dumps(data))
# 保存JSON的格式,再加一个参数indent,代表缩进字符个数
# with open('data1.json', 'w') as file:
#     file.write(json.dumps(data, indent=2))
# JSON中包含中文字符,中文字符都变成了Unicode字符,需要指定ensure_ascii为False,另外还要规定文件输出的编码
with open('data1.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))