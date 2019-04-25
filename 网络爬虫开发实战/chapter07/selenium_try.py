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
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser, 10) # 引入WebDriverWait对象,指定最长等待时间,然后调用until()方法,传入要等待条件expected_conditions.
# input = wait.until(EC.presence_of_element_located((By.ID, 'q'))) # 这里传入presence_of_element_located这个条件,代表节点出现,参数是节点的定位元组,也就是ID为q的节点搜索框
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search'))) # 这里传入的条件是element_to_be_clickable,也就是可点击,查找按钮时查找CSS选择器为.btn-search的按钮
# print(input, button)
# 12.前进和后退:back()后退,forward()前进
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org')
# browser.back()
# time.sleep(1)
# browser.forward()
# time.sleep(1)
# browser.close()
# 13.Cookies:对Cookies进行操作,获取,添加,删除Cookies等
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())
# 14.选项卡管理:
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()') # 调用execute_script()方法,传入js语句window.open()新开启一个选项卡
# print(browser.window_handles) # window_handles获取当前开启的所有选项卡
# browser.switch_to.window(browser.window_handles[1]) # 跳转至第2个选项卡
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to.window(browser.window_handles[0]) # 跳转至第1个选项卡
# browser.get('https://python.org')
# time.sleep(3)
# browser.close()
# browser.quit()
# 15.异常处理:超时,节点未找到等错误,一旦出现此类错误,程序便不会继续执行了.可以try except语句来获取各种异常
# from selenium import webdriver
# from selenium.common.exceptions import  TimeoutException, NoSuchElementException
# browser = webdriver.Firefox()
# browser.get('https://www.baidu.com')
# browser.find_element_by_id('hello') # id='hello'的元素不存在,抛出NoSuchElementException异常,节点未找到
# try:
#     browser.get('https://www.baidu.com')
# except TimeoutException:
#     print('Time Out')
# try:
#     browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print('No Element')
# finally:
#     browser.close()
# from selenium import webdriver
# browser = webdriver.PhantomJS()
# browser.get('https://www.baidu.com')
# print(browser.current_url)
# browser.close()

# # 使用Firefox的无头版本地带PhantomJS
# from selenium.webdriver import Firefox
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.wait import WebDriverWait
#
# if __name__ == '__main__':
#     options = Options()
#     options.add_argument('-headless') # 无头参数
#     # driver = Firefox(executable_path='geckodriver', firefox_options=options) # 设置了环境变量,第一个参数可以省略,否则传绝对路径
#     driver = Firefox(options=options)
#     wait = WebDriverWait(driver, timeout=10)
#     driver.get('http://www.google.com')
#     wait.until(ec.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
#     wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
#     print(driver.page_source)
#     driver.quit()

# # 使用Chrome的无头版本代替PhantomJS
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument('-headless')
# driver = webdriver.Chrome(options=options)
# driver.get('https://www.baidu.com')
# print(driver.current_url)
# driver.close()