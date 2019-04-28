# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/28 7:04
# @Author   : tangky
# @Site     : 
# @File     : jycode_test.py
# @Software : PyCharm


from io import BytesIO
from PIL import Image
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
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
        获取验证码位置,首先获取图片对象的位置和宽高,随后返回其左上角和右下角的坐标
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gt_ajax_tip gt_ready')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片:获取网页截图,调用crop()方法将图片裁切出来,返回Image对象
        :param name:
        :return: 图片对象
        """
        top, bottom, left, right = self.get_postition()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        return captcha
    def get_slider(self):
        """
        获取滑块
        :return:滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'gt_slider_knob gt_show')))
        return slider
    """
    得到两张图片对象,分别赋值给变量image1和image2,接下来对比图片获取缺口.遍历图片的每个坐标点,
    获取两张图片对应像素点的RGB数据.如果二者的RGB数据差距在一定范围内,那就代表两个像素相同,继续比对下一个像素点.
    如果差距超过一定范围,则代表像素点不同,当前位置即为缺口位置
    """
    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False
    def get_gap(self, image1, image2):
        """
        获取缺口偏移量
        :param image1: 不带缺口图片
        :param image2: 带缺口图片
        :return:
        """
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left
    """
    get_gap()方法即获取缺口位置的方法.此方法的参数是两张图片,一张为带缺口图片,另一张为不带缺口图片.
    这里遍历两张图片的每个像素点,利用is_pixel_equal()方法判断两张图片同一位置的像素是否相同.比较两张图片RGB的
    绝对值是否均小于定义的阈值threshold.如果绝对值均在阈值之内,则代表像素点相同,继续遍历.否则代表不同的像素点,
    即缺口的位置
    """
    # 模拟拖动
    """
    不能匀速拖动,
    完全模拟加速减速的过程通过了验证.前段滑块做匀加速运动,后端滑块做匀减速运动,利用物理学的加速度公式即可完成验证.
    x = v0 * t + 0.5 * a * t * t
    v = v0 + a * t
    利用这两个公式可以构造轨迹移动算法,计算出先加速后减速的运动轨迹
    """
    def get_track(self,distance):
        """
        根据偏移量获取移动速度
        """
        # 移动速度
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0
        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度 v = v0 + a * t
            v = v0 + a * t
            # 移动距离x = v0 * t + 1 / 2 * a * t ^ 2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def move_to_gap(self, slider, tracks):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param tracks: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()