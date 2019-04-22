# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 20:29
# @Author   : tangky
# @Site     : 
# @File     : requests_test.py
# @Software : PyCharm

# import requests

# requests中相应的get()方法就是urllib库中的urlopen()方法
# r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# r = requests.get('http://httpbin.org/get')
# r = requests.get('http://httpbin.org/get?name=germey&age=22')
# print(r.text)
# data = {'name': 'germey', 'age': '22'}
# r = requests.get('http://httpbin.org/get', params=data)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))
# print(r.text)

# 网页返回类型为str类型,是JSON格式的,想直接解析返回结果,得到一个字典格式,调用json()方法
# 如果返回不是JSON类型,便会出现解析错误,抛出json.decoder.JSONDecodeError异常

# 抓取网页
# import requests
# import re
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# print(r.text)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S) # .匹配/n之外任何单字符,re.S(DOTALL)'.'任意匹配模式
# titles = re.findall(pattern, r.text)
# print(titles)

# 抓取二进制数据
# GitHub站点图标
# import requests
# r = requests.get('https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo_top_86d58ae1.png')
# # print(r.text)
# # print(r.content)
# # 保存图片
# with open('test.png', 'wb') as f:
#     f.write(r.content)

# 4.POST请求
# import requests
#
# data = {'name': 'germey', 'age': '22'}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)

# 5.响应
# import requests
#
# r = requests.get('http://www.jianshu.com')
# print(type(r.status_code), r.status_code)  # 状态码
# print(type(r.headers), r.headers)  # 响应头,CaseInsensitiveDict类型
# print(type(r.cookies), r.cookies)  # Cookies, RequestsCookieJar类型
# print(type(r.url), r.url)  # URL
# print(type(r.history), r.history)  # 请求历史

# requests内置的状态吗查询对象requests.codes
# import requests
# r = requests.get('http://www.jianshu.com')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

# 3.2.2高级用法
# 1.文件上传
import requests

# files = {'file': open('test.png', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)
# 2.Cookies
# r = requests.get('http://www.baidu.com')
# print(r.cookies)  # RequestCookieJar类型
# for key, value in r.cookies.items():
#     print(key + '=' + value)
# headers = {'Cookie': 'd_c0="AKDkSye6uA2PTm7rCWD56KUdEwTuPmKE5v0=|1528515129"; _zap=1a5483ee-47ed-405c-8d56-71f8b1ed901c; _xsrf=4EuFLbAn0GQQPlxbDNVDO6jRCWC6KE1b; capsion_ticket="2|1:0|10:1555240299|14:capsion_ticket|44:ZTkzYjhmYWYzODE1NDA0MzkzY2M5MDViZDk3ZTY4NWU=|85745b28f11f280c366ae976b36ad7eb026fee2d34af0f13326d59e6e1595280"; r_cap_id="Yzg0ZDg0OWVjODZhNGQ3MDgxNDgxNmQ1MjJhMjk3OGQ=|1555240316|661bfaef8ce5d6737ff9e090a583a5663dfaa00e"; cap_id="YTRiM2EzYTAyOTU2NGE3Yjk1ZmY5NzMyMTgzMDEzMWU=|1555240316|84f88484e4a5396d22cbb2bde0f4ebfb82f0a379"; l_cap_id="N2RmZWYyYmE3MzZlNGMyZWE4NDkxYjkwMjBkNjk1Y2I=|1555240316|c415759bf7707e2d9cba75e1a143c12bccd722e9"; z_c0=Mi4xWVFsYkFBQUFBQUFBb09STEo3cTREUmNBQUFCaEFsVk5oMk9nWFFCNXBIWVMyeS1zOHh2ZmpNYi1oMzdrYjdBQWx3|1555240327|c53d9237ad08b0a296ca969de8c272a715489b16; tst=r; __gads=ID=cfd1ee4e88c6ff07:T=1555240330:S=ALNI_MbtWYJIVW008TWFZ2i9faHZvN3mSQ; q_c1=08f73525335f44bbb8be9692c6008515|1555836348000|1528515129000; __utma=155987696.595845276.1555851819.1555851819.1555851819.1; __utmc=155987696; __utmz=155987696.1555851819.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=a37704a413efa26cf3f23813004f1a3b',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
# r = requests.get('http://www.zhihu.com', headers=headers)
# print(r.text)
# with open('zhihu.html', 'wb') as f:
#     f.write(r.text.encode(encoding='utf-8'))

# 也可以通过cookies参数来设置,需要构造RequestsCookieJar对象,而且需要分割一下cookies.
# cookies = 'd_c0="AKDkSye6uA2PTm7rCWD56KUdEwTuPmKE5v0=|1528515129"; _zap=1a5483ee-47ed-405c-8d56-71f8b1ed901c; _xsrf=4EuFLbAn0GQQPlxbDNVDO6jRCWC6KE1b; capsion_ticket="2|1:0|10:1555240299|14:capsion_ticket|44:ZTkzYjhmYWYzODE1NDA0MzkzY2M5MDViZDk3ZTY4NWU=|85745b28f11f280c366ae976b36ad7eb026fee2d34af0f13326d59e6e1595280"; r_cap_id="Yzg0ZDg0OWVjODZhNGQ3MDgxNDgxNmQ1MjJhMjk3OGQ=|1555240316|661bfaef8ce5d6737ff9e090a583a5663dfaa00e"; cap_id="YTRiM2EzYTAyOTU2NGE3Yjk1ZmY5NzMyMTgzMDEzMWU=|1555240316|84f88484e4a5396d22cbb2bde0f4ebfb82f0a379"; l_cap_id="N2RmZWYyYmE3MzZlNGMyZWE4NDkxYjkwMjBkNjk1Y2I=|1555240316|c415759bf7707e2d9cba75e1a143c12bccd722e9"; z_c0=Mi4xWVFsYkFBQUFBQUFBb09STEo3cTREUmNBQUFCaEFsVk5oMk9nWFFCNXBIWVMyeS1zOHh2ZmpNYi1oMzdrYjdBQWx3|1555240327|c53d9237ad08b0a296ca969de8c272a715489b16; tst=r; __gads=ID=cfd1ee4e88c6ff07:T=1555240330:S=ALNI_MbtWYJIVW008TWFZ2i9faHZvN3mSQ; q_c1=08f73525335f44bbb8be9692c6008515|1555836348000|1528515129000; __utma=155987696.595845276.1555851819.1555851819.1555851819.1; __utmc=155987696; __utmz=155987696.1555851819.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=a37704a413efa26cf3f23813004f1a3b'
# from requests.cookies import RequestsCookieJar
# jar = RequestsCookieJar()
# headers = {
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# }
# for cookie in cookies.split(';'):
#     print(cookie.split('='))
#     key, value = cookie.split('=', 1) # 1表示分割次数, 默认为-1尽可能分割
#     print(key, value)
#     jar.set(key, value)
# r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
# print(r.text)

# 3.会话维持
# requests.get('http://httpbin.org/cookies/set/number/123456789') # 设置一个cookie,名称为number,内容为123456789
# r = requests.get('http://httpbin.org/cookies') # 重新请求,无法获取cookies
# print(r.text)

# s = requests.Session() # s是Session对象,一个会话,模拟同一个会话而不用担心Cookies地问题.通常用于模拟登陆成之后再进行下一步操作
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)
# 设置忽略警告屏蔽警告
# import urllib3
#
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)
# 通过捕获警告到日志地方式忽略警告:
import logging
logging.captureWarnings(True)
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# 可以指定一个本地证书用作客户端证书,可以是单个文件(包含密钥和证书)