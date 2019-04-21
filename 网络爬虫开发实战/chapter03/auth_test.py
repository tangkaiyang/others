# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/21 13:39
# @Author   : tangky
# @Site     : 
# @File     : auth_test.py.py
# @Software : PyCharm

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p) # 实例化HTTPBasicAuthHandler对象,其参数是HTTPPasswordMgrWithDefaultRealm对象,它利用add_password()添加进去用户名和密码,这样就建立了一个处理验证的Handler
opener = build_opener(auth_handler) # 利用这个Handler并使用build_opener()方法构建一个Opener,这个Opener再发送请求时就相当于已经验证成功了

try:
    result = opener.open(url) # 利用Opener的open()方法打开链接,就可以完成验证了
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)