# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/28 7:04
# @Author   : tangky
# @Site     : 
# @File     : jycode_test.py
# @Software : PyCharm


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# b站模拟登录
# 极验验证码的识别
# 初始化:初始化一些配置
ACCOUNT = '17757989076'
PASSWORD = 'tangkaiyang123'


class CrackGeetest():
    def __init__(self):
        self.url = 'https://passport.bilibili.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.account = ACCOUNT
        self.password = PASSWORD

    # 模拟点击初始的验证按钮,定义一个方法来获取这个按钮,利用显式等待的方法来实现
    def get_geetest_button(self):
        """
        获取初始验证码按钮
        :return: 按钮对象
        """
        button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gt_ajax_tip gt_ready')))
        return button

    # 识别缺口:对比前后两张图片,二者不一致的地方即为缺口.
    # 获取不带缺口的图片,利用Selenium选取图片元素,得到其所在位置的宽高,然后获取整个网页的截图,图片裁切出来即可
    def get_postition(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gt_ajax_tip gt_ready')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :param name:
        :return: 图片对象
        """
        top, bottom, left, right = self.get_postition()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        return captcha
