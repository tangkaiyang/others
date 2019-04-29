# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/29 7:26
# @Author   : tangky
# @Site     : 
# @File     : scheduler.py
# @Software : PyCharm

TESTER_CYCLE = 20
GETTER_CYCLE = 20
# TESTER_ENABLED, GETTER_ENABLED, API_ENABLED都是布尔类型,表示测试模块,获取模块,接口模块的开关,True表示模块开启
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True
API_HOST = '0.0.0.0'
API_PORT = 5555

from multiprocessing import Process, freeze_support
from api import app
from getter import Getter
from tester import Tester
import time


class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理:首先声明一个Tester对象,然后进入死循环不断循环调用其run()方法,执行完一轮之后就休眠一段时间,
        休眠结束后重新执行.在这里,休眠时间也定义为一个常量,如20秒,即每隔20秒进行一次代理检测
        :param cycle:
        :return:
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        :param cycle:
        :return:
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启API
        :return:
        """
        app.run(API_HOST, API_PORT)

    def run(self):
        """
        启动入口是run()方法,这个方法分别判断3个模块的开关.如果开启开关,启动程序就新建一个Process进程,
        设置好启动目标,然后调用start()方法运行,这样3个进程就可以并行执行,互不干扰
        :return:
        """
        print('代理池开始运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
    # 只需要调用Scheduler的run()方法即可启动整个代理池


if __name__ == '__main__':
    freeze_support()
    Scheduler().run()