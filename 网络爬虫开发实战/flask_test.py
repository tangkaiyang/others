# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/26 11:30
# @Author   : tangky
# @Site     : 
# @File     : flask_test.py
# @Software : PyCharm

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
