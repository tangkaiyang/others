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
# import requests
#
# # files = {'file': open('test.png', 'rb')}
# # r = requests.post('http://httpbin.org/post', files=files)
# # print(r.text)
# # 2.Cookies
# # r = requests.get('http://www.baidu.com')
# # print(r.cookies)  # RequestCookieJar类型
# # for key, value in r.cookies.items():
# #     print(key + '=' + value)
# # headers = {'Cookie': 'd_c0="AKDkSye6uA2PTm7rCWD56KUdEwTuPmKE5v0=|1528515129"; _zap=1a5483ee-47ed-405c-8d56-71f8b1ed901c; _xsrf=4EuFLbAn0GQQPlxbDNVDO6jRCWC6KE1b; capsion_ticket="2|1:0|10:1555240299|14:capsion_ticket|44:ZTkzYjhmYWYzODE1NDA0MzkzY2M5MDViZDk3ZTY4NWU=|85745b28f11f280c366ae976b36ad7eb026fee2d34af0f13326d59e6e1595280"; r_cap_id="Yzg0ZDg0OWVjODZhNGQ3MDgxNDgxNmQ1MjJhMjk3OGQ=|1555240316|661bfaef8ce5d6737ff9e090a583a5663dfaa00e"; cap_id="YTRiM2EzYTAyOTU2NGE3Yjk1ZmY5NzMyMTgzMDEzMWU=|1555240316|84f88484e4a5396d22cbb2bde0f4ebfb82f0a379"; l_cap_id="N2RmZWYyYmE3MzZlNGMyZWE4NDkxYjkwMjBkNjk1Y2I=|1555240316|c415759bf7707e2d9cba75e1a143c12bccd722e9"; z_c0=Mi4xWVFsYkFBQUFBQUFBb09STEo3cTREUmNBQUFCaEFsVk5oMk9nWFFCNXBIWVMyeS1zOHh2ZmpNYi1oMzdrYjdBQWx3|1555240327|c53d9237ad08b0a296ca969de8c272a715489b16; tst=r; __gads=ID=cfd1ee4e88c6ff07:T=1555240330:S=ALNI_MbtWYJIVW008TWFZ2i9faHZvN3mSQ; q_c1=08f73525335f44bbb8be9692c6008515|1555836348000|1528515129000; __utma=155987696.595845276.1555851819.1555851819.1555851819.1; __utmc=155987696; __utmz=155987696.1555851819.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=a37704a413efa26cf3f23813004f1a3b',
# #            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
# # r = requests.get('http://www.zhihu.com', headers=headers)
# # print(r.text)
# # with open('zhihu.html', 'wb') as f:
# #     f.write(r.text.encode(encoding='utf-8'))
#
# # 也可以通过cookies参数来设置,需要构造RequestsCookieJar对象,而且需要分割一下cookies.
# # cookies = 'd_c0="AKDkSye6uA2PTm7rCWD56KUdEwTuPmKE5v0=|1528515129"; _zap=1a5483ee-47ed-405c-8d56-71f8b1ed901c; _xsrf=4EuFLbAn0GQQPlxbDNVDO6jRCWC6KE1b; capsion_ticket="2|1:0|10:1555240299|14:capsion_ticket|44:ZTkzYjhmYWYzODE1NDA0MzkzY2M5MDViZDk3ZTY4NWU=|85745b28f11f280c366ae976b36ad7eb026fee2d34af0f13326d59e6e1595280"; r_cap_id="Yzg0ZDg0OWVjODZhNGQ3MDgxNDgxNmQ1MjJhMjk3OGQ=|1555240316|661bfaef8ce5d6737ff9e090a583a5663dfaa00e"; cap_id="YTRiM2EzYTAyOTU2NGE3Yjk1ZmY5NzMyMTgzMDEzMWU=|1555240316|84f88484e4a5396d22cbb2bde0f4ebfb82f0a379"; l_cap_id="N2RmZWYyYmE3MzZlNGMyZWE4NDkxYjkwMjBkNjk1Y2I=|1555240316|c415759bf7707e2d9cba75e1a143c12bccd722e9"; z_c0=Mi4xWVFsYkFBQUFBQUFBb09STEo3cTREUmNBQUFCaEFsVk5oMk9nWFFCNXBIWVMyeS1zOHh2ZmpNYi1oMzdrYjdBQWx3|1555240327|c53d9237ad08b0a296ca969de8c272a715489b16; tst=r; __gads=ID=cfd1ee4e88c6ff07:T=1555240330:S=ALNI_MbtWYJIVW008TWFZ2i9faHZvN3mSQ; q_c1=08f73525335f44bbb8be9692c6008515|1555836348000|1528515129000; __utma=155987696.595845276.1555851819.1555851819.1555851819.1; __utmc=155987696; __utmz=155987696.1555851819.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=a37704a413efa26cf3f23813004f1a3b'
# # from requests.cookies import RequestsCookieJar
# # jar = RequestsCookieJar()
# # headers = {
# #     'Host': 'www.zhihu.com',
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# # }
# # for cookie in cookies.split(';'):
# #     print(cookie.split('='))
# #     key, value = cookie.split('=', 1) # 1表示分割次数, 默认为-1尽可能分割
# #     print(key, value)
# #     jar.set(key, value)
# # r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
# # print(r.text)
#
# # 3.会话维持
# # requests.get('http://httpbin.org/cookies/set/number/123456789') # 设置一个cookie,名称为number,内容为123456789
# # r = requests.get('http://httpbin.org/cookies') # 重新请求,无法获取cookies
# # print(r.text)
#
# # s = requests.Session() # s是Session对象,一个会话,模拟同一个会话而不用担心Cookies地问题.通常用于模拟登陆成之后再进行下一步操作
# # s.get('http://httpbin.org/cookies/set/number/123456789')
# # r = s.get('http://httpbin.org/cookies')
# # print(r.text)
# # 设置忽略警告屏蔽警告
# # import urllib3
# #
# # urllib3.disable_warnings()
# # response = requests.get('https://www.12306.cn', verify=False)
# # print(response.status_code)
# # 通过捕获警告到日志地方式忽略警告:
# import logging
# logging.captureWarnings(True)
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)

# 可以指定一个本地证书用作客户端证书,可以是单个文件(包含密钥和证书)或一个包含两个文件路径的元组
# import requests
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/paht/key'))
# print(response.status_code)
# 注意,本地私有证书的key必须是解密状态的,加密状态的key是不支持的
# 5.代理设置
# import requests
# proxies = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'http://10.10.1.10:1080'
# }
# requests.get('https://www.taobao.com', proxies=proxies)
# 若代理需要使用HTTP Basic Auth,可以使用类似http://user:password@host:port这样的语法来设置代理
# import requests
# proxies = {
#     'http': 'http://user:password@10.10.1.10:3128',
# }
# requests.get('https://www.taobao.com', proxies=proxies)
# requests还支持SOCKS协议的代理
# import requests
# proxies = {
#     'http': 'socks5://user:password@host:port',
#     'https': 'socks5://user:password@host:port'
# }
# requests.get('https://www.taobao.com', proxies=proxies)

# 6.超时设置
import requests
# import urllib3
# urllib3.disable_warnings()
# r = requests.get('https://www.taobao.com', timeout=1, verify=False)
# print(r.status_code)
# 实际上,请求分为两个阶段,即连接(connect)和读取(read)
# 上面设置的timeout将用作连接和读取这二者的timeout总和
# 如果要分别制定,就可以传入一个元组
# r = requests.get('https://www.taobao.com', timeout=(5, 11), verify=False)
# print(r.status_code)
# 如果想要永久等待,可以直接将timeout设置为None,或者不设置直接留空,因为默认为None.
# 这样的话,如果服务器还在运行,但是响应特别慢,那就慢慢等吧,它永远不会返回超时错误的.
# r = requests.get('https://www.taobao.com', timeout=None, verify=False)
# print(r.status_code)
# 7.身份认证
# 使用requests自带的身份认证功能
# import requests
# from requests.auth import HTTPBasicAuth
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)
# 认证成功返回200,失败返回400
# 更简单的写法,直接传一个元组,默认使用HTTPBasicAuth这个类来认证
# import requests
# r = requests.get('http://localhost:5000', auth=('username', 'password'))
# print(r.status_code)
# 8.Prepared Request
# from requests import Request, Session
# url = 'http://httpbin.org/post'
# data = {
#     'name': 'germey'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# }
# s = Session()
# req = Request('POST', url, data=data, headers=headers)
# prepared = s.prepare_request(req)
# r = s.send(prepared)
# print(r.text)
# 这里引入了Request,然后用url,data和headers参数构造了一个Request对象,这时需要再调用Session的prepare_request()方法将其转换为一个Prepared Request对象,然后调用send()方法发送即可
# 有了Request这个对象,就可以将请求当做独立的对象来看待,这样在进行队列调度时会非常方便
# 3.3正则表达式
# 2.match()
# import re

# content = 'Hello 123 4567 World_This is a Regex Demo'
# content = 'Hello 1234567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(type(result)) # re.Match对象
# print(result)
# print(result.group()) # 输出匹配的内容
# print(result.span()) # 输出匹配的范围
# 匹配目标,从匹配的字符串中提取一部分内容,使用()将想提取的子字符串括起来.
# ()实际上标记了一个子表达式的开始和结束位置,,被标记的每个子表达式会依次对应每一个分组,调用group()方法传入分组的索引即可获取提取的结果
# result = re.match(r"^Hello\s(\d+)\sWorld", content)
# print(result)
# print(result.group())  # 输出完整的匹配结果
# print(result.group(1))  # 输出第一个被()包围的匹配结果
# print(result.span())
# 通用匹配
# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match(r'^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())
# 贪婪与非贪婪
# import re
#
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$', content)
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
# 贪婪匹配下,.*会匹配尽可能多的字符
# 非贪婪,.*?,在做匹配的时候,字符串中间尽量使用非贪婪匹配,也就是用.*?代替.*,以免出现匹配结果缺失的情况
# 注意:如果匹配的结果在字符串结尾,.*?就可能匹配不到任何内容了,因为它会匹配尽可能少的字符
# import re
# content = 'http://weibo.com/comment/kEraCN'
# result1 = re.match(r'http.*?comment/(.*?)', content)
# result2 = re.match(r'http.*?comment/(.*)', content)
# print('result1', result1.group(1))
# print('result2', result2.group(1))
# 修饰符
import re
content = '''Hello 1234567 World_This
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result)
# 加了一个换行符,匹配不到,因为,匹配的是除换行符之外的任意字符,当遇到换行符时,.*?就不能匹配了,所以导致匹配失败.这里需要加一个修饰符re.S,即可修正