# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/28 10:29
# @Author   : tangky
# @Site     : 
# @File     : chaojiying.py
# @Software : PyCharm

# 超级鹰API
import requests
from hashlib import md5


class Chaojiying():

    def __init__(self, username, password, soft_id):
        self.username = username
        self.password = md5(password.encode('utf-8')).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }

    def post_pic(self, im, codetype):
        """
        :param im: 图片字节
        :param codetype: 题目类型 参考http://www.chaojiying.com/price.html
        :return:
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfule': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def report_error(self, im_id):
        """
        :param im_id:报错题目的图片ID
        :return:
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()
