# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/29 7:17
# @Author   : tangky
# @Site     : 
# @File     : api.py
# @Software : PyCharm


# 使用比较轻量级的库Flask来实现这个接口模块
from flask import Flask, g
from db import RedisClient

__all__ = ['app']
app = Flask(__name__) # 声明了Flask对象


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index(): # 接口:首页
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    """
    获取随机可用代理,接口,随机代理页
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()

@app.route('/count')
def get_counts():
    """
    获取代理池总量,接口,获取数量页
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run() # 运行之后,Flask会启动一个Web服务,需要访问对应的接口即可获取到可用代理
