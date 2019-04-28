# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/28 14:16
# @Author   : tangky
# @Site     : 
# @File     : proxy_try.py
# @Software : PyCharm

# 利用西刺代理http://www.xicidaili.com的代理服务发送HTTP请求
# 2.urllib,以urllib为例,设置代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
# 借助ProxyHandler设置代理,参数是字典类型,键名为协议类型,键值是代理.
# proxy = '211.24.103.228:80'
# proxy = 'username:password@211.24.103.228:80' # 需要认证的代理
# proxy_handler = ProxyHandler({
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy
# })
# opener = build_opener(proxy_handler) # 利用build_opener()方法传入该对象来创建一个Opener
# try:
#     response = opener.open('http://httpbin.org/get') # 调用Opener对象的open()方法,访问想要的链接
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

# 代理是SOCKS5类型
# import socks # 需要一个socks模块:pip install PySocks
# import socket
# from urllib import request
# from urllib.error import URLError
#
# socks.set_default_proxy(socks.SOCKS5, '115.236.100.104', 8080)
# socket.socket = socks.socksocket
# try:
#     response = request.urlopen('http://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)
# 3.requests:只需传入proxies参数
# import requests
# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy,
# }
# try:
#     response = requests.get('http://httpbin.org/get', proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('Error', e.args)
# 需要认证时:proxy = 'username:password@......'
# 需要使用SOCKS5代理:pip install requests[socks]
# import requests
# proxies = {
#     'http': 'socks5://' + proxy,
#     'https': 'socks5://' + proxy
# }
# try:
#     response = requests.get('http://httpbin.org/get', proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('Error', e.args)

# # 和urllib中的方法相同,使用socks模块,也需要像上文一样安装socks库
# import requests
# import socks
# import socket
# socks.set_default_proxy(socks.SOCKS5, '115.236.100.104', 8080)
# socket.socket = socks.socksocket
# try:
#     response = requests.get('http://httpbin.org/get')
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('Error', e.args)

# 4.Selenium:Selenium同样也可以设置代理,包括两种方式:一种是有界面浏览器,以Chrome为例;另一种是无界面浏览器,以PhantomJS为例
# # Chrome
# from selenium import webdriver
#
# proxy = '211.24.103.228:80'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://' + proxy)
# browser = webdriver.Chrome(options=chrome_options)
# browser.get('http://httpbin.org/get')
# # 代理认证的设置
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import zipfile

ip = '211.24.103.228'
port = 80
username = 'foo'
password = 'bar'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions" : [
        "proxy",
        "tabs",
        "unlimitedStorages",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
        ],
    "background": {
        "scripts": ["background.js"]
    }
}
"""

background_js = """
var config = {
    mode: "fixed_servers",
    rules: {
        singleProxy: {
            scheme: "http",
            host: "%(ip)s",
            port: %(port)s
            }
        }
    }
chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
function callbackFn(details) {
    return {
        authCredentials: {
            username: "%(username)s",
            password: "%(password)s"
        }
    }
}
chrome.webRequest.onAuthRequired.addListener(
    callbackFn,
    {urls: ["<all_urls>"]},
    ['blocking']
)
""" % {'ip': ip, 'port': port, 'username': username, 'password': password}

plugin_file = 'proxy_auth_plugin.zip'
with zipfile.ZipFile(plugin_file, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_extension(plugin_file)
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://httpbin.org/get')
# # 这里需要在本地创建一个manifest.json配置文件和background.js脚本来设置认证代理.运行代码后本地会生成一个proxy_auth_plugin.zip文件来保存当前配置
# # PhantomJS(略)设置Chrome为无头模式