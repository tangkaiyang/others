# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/24 19:55
# @Author   : tangky
# @Site     : 
# @File     : redis_try.py
# @Software : PyCharm

# 3.链接Redis:
# from redis import StrictRedis
# redis = StrictRedis(host='localhost', port=6379, db=0)
# redis = StrictRedis() # 默认的host地址为localhost,port运行端口为6379,db使用的数据库为0,密码password为None
# # 声明了一个StrictRedis对象
# redis.set('name', 'Bob') # 调用set()方法,设置一个键值对
# print(redis.get('name'))
# # 使用ConnectionPool来连接
from redis import StrictRedis, ConnectionPool
# pool = ConnectionPool()
# redis = StrictRedis(connection_pool=pool)
# StrictRedis内其实就是用host和port等参数又构造了一个ConnectionPool,所有直接将ConnectionPool当参数传给StrictRedis也一样
# 另外,ConnectionPool还支持通过URL来构建
# # redis://[:password]@host:port/db 创建Redis TCP连接
# # rediss://[:password]@host:port/db Redis TCP+SSL连接
# # unix://[:password]@/path/to/socket.sock?db=db Redis UNIX socket连接
url = 'redis://@localhost:6379/0'
pool = ConnectionPool(url)
redis = StrictRedis(connection_pool=pool)