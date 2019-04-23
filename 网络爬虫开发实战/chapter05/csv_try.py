# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 20:46
# @Author   : tangky
# @Site     : 
# @File     : csv_try.py
# @Software : PyCharm

# 1.写入
# import csv
# with open('data.csv', 'w') as csvfile:
    # writer = csv.writer(csvfile, delimiter='\t') # delimiter设定分隔符
    # writer.writerow(['id', 'name', 'age'])
    # writer.writerow(['10001', 'Mike', 20])
    # writer.writerow(['10002', 'Bob', 20])
    # writer.writerow(['10003', 'Jordan', 21])
    # writer.writerows([['10004', 'Ben', 23], ['10005', 'White', 32]]) # writerows写入多行,传入参数为一个二维列表
    # 一般情况下,爬虫爬取的都是结构化数据,一般用字典表示
    # fieldnames = ['id', 'name', 'age']
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # writer.writeheader() # 写入头信息
    # writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
# 写入中文内容,可能会遇到字符编码的问题,需要给open()参数指定编码格式
# import csv
# with open('data.csv', 'a', encoding='utf-8') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})
# 2.读取
import csv
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)