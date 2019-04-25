# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/25 14:11
# @Author   : tangky
# @Site     : 
# @File     : selenium_try.py
# @Software : PyCharm

# 7.1 Selenium的使用
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url) # 当前url
#     print(browser.get_cookies()) # 当前的Cookies
#     # print(browser.page_source) # 网页源代码
# finally:
#     browser.close()
# 5.查找节点
# # 单个节点
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first, input_second, input_third, sep='\n')
# browser.close()
# # 还提供了find_element(By.ID, id),是find_element_by_id(id)的通用函数版本
# # 多个节点:find_elements()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# # lis = browser.find_elements_by_css_selector('.service-bd li')
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li') # 与上一条一致
# print(lis)
# browser.close()
# 6.节点交互:send_keys(),clear(),click()
# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# time.sleep(1)
# browser.close()
# 7.动作链:没有特定的执行对象,比如鼠标拖拽,键盘按键等
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult') # id='iframeResult'
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()
# import time
# time.sleep(3)
# alert = browser.switch_to.alert # !!!
# alert.accept()
# time.sleep(1)
# browser.close()
# 8.执行JavaScript:下拉进度条等,直接模拟运行JavaScript,使用execute_script()方法
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 将进度条下拉到最底层
# browser.execute_script('alert("To Bottom")') # 弹出alert提示框
# browser.switch_to.alert.accept()
# import time
# time.sleep(1)
# browser.close()
# 9.获取节点信息:page_source属性获取网页的源代码,接着使用解析库提取信息
# Selenium选择节点的方法,返回WebElement类型,也有相关的方法和属性来直接提取节点信息,如属性,文本等.
# # 获取属性:get_attribute()方法来获取节点的属性,前提要先选中这个节点
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
# print(logo.get_attribute('class'))
# # 获取文本值:WebElement节点都有text属性,直接调用这个属性就可以得到节点内部的文本信息
# from selenium import webdriver
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)
# # 获取id,位置,标签和大小
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)
# browser.close()
# 10.切换Frame
# # 网页中有一种节点叫做iframe,也就是子Frame,相当于页面的子页面,它的结构和外部网页的结构完全一致.
# # Selenium打开页面后,默认是在父级Frame里面操作,而此时如果页面中还有子Frame,它不能获取到子Frame里面的节点
# # switch_to.frame()方法来切换Frame
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)
# 11.延时等待:get()方法会在网页框架加载结束后结束执行,此时如果获取page_source,可能并不是浏览器完全加载完成的页面,如果某些页面有额外的
# Ajax请求,我们在网页源代码中也不一定能成功获取到.所以,这里需要延时等待一定时间,确保节点已经加载出来.
# # 等待的两种方式:隐式等待,显式等待
# # 隐式等待:当使用隐式等待执行测试的时候,如果Selenium没有在DOM中找到节点,将继续等待,超出设定时间后,则抛出找不到节点的异常.
# # 换句话说,当查找节点而节点没有立即出现的时候,隐式等待将等待一段时间再查找DOM,默认的时间是0.
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.implicitly_wait(10) # implicitly_wait()方法实现隐式等待
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)
# browser.close()
# # 显式等待:隐式等待的效果其实并没有那么好,因为我们只规定了一个固定时间,而页面的加载时间会受到网络条件的影响
# # 显示等待:指定要查找的节点,然后指定一个最长等待时间.
# # 如果在规定时间内加载出来了这个节点,就返回查找的节点;如果到了规定时间依然没有加载出该节点,则抛出超时异常
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located(()))