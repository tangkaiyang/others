# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/28 17:08
# @Author   : tangky
# @Site     : 
# @File     : error.py
# @Software : PyCharm


class PoolEmptyError(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经枯竭')
