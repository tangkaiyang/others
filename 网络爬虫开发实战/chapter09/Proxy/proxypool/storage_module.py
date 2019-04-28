# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/28 16:24
# @Author   : tangky
# @Site     : 
# @File     : storage_module.py
# @Software : PyCharm

# 定义一个类来操作数据库的有序集合,定义一些方法来实现分数的设置,代理的获取等
MAX_SCORE = 100  # 最大分数
MIN_SOCRE = 0  # 最小分数
INITIAL_SCORE = 10  # 初始分数
REDIS_HOST = 'localhost'  # Redis的连接信息,地址
REDIS_PORT = 6379  # 端口
REDIS_PASSWORD = None  # 密码
REDIS_KEY = 'proxies'  # 有序集合的键名,可以通过它来获取代理存储所使用的有序集合

import redis
from error import PoolEmptyError
from random import choice


class RedisClient():
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化,参数是Redis的连接信息,默认的连接信息已经定义为常量,初始化一个StrictRedis类,建立Redis连接
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis 密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理,设置分数为最高,默认的分数是INITIAL_SCORE,也就是10,返回结果是添加的结果
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, proxy)

    def random(self):
        """
        随机获取有效代理,首先尝试获取最高分数代理,如果最高分数不存在,则按照排名获取,否则异常
        :return: 随机代理
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

    def decrease(self, proxy):
        """
        代理值减一分,分数小于最小值,则代理删除
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SOCRE:
            print('代理', proxy, '当前分数', score, "减1")
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """
        print('代理', proxy, '可用,设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        """
        获取数量
        :return:数量
        """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        return self.db.zrangebyscore(REDIS_KEY, MIN_SOCRE, MAX_SCORE)
