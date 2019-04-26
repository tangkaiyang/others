# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/26 14:56
# @Author   : tangky
# @Site     : 
# @File     : tesserocr_test.py
# @Software : PyCharm

import tesserocr
from PIL import Image

# image = Image.open('C:/Users/user/Desktop/test.png')
# image1 = Image.open('./hh.png') # 新建Image对象
# image2 = Image.open('./long.png')
# image3 = Image.open('./lll.png')
# print(tesserocr.image_to_text(image1, lang='chi_sim')) # 调用tesserocr的image_to_text()方法,传入Image对象即可完成识别,lang指定语言,默认为eng,简体中文为chi_sim
# print(tesserocr.image_to_text(image2, lang='eng'))
# print(tesserocr.image_to_text(image3, lang='eng'))
# 5.验证码处理
import tesserocr
from PIL import Image
image =Image.open('code2.jpg')
# result = tesserocr.image_to_text(image)
# print(result)
# # 利用Image对象的convert()方法参数传入L,即可将图片转化为灰度图像
# image = image.convert('L')
# image.show()
# # convert()传入1即可将图片进行二值化处理
# image = image.convert('1')
# image.show()
# # 还可以指定二值化的阈值.上面的方法采用的默认阈值是127.不过我们能直接转化原图,要将原图先转化为灰度图像,然后再指定二值化阈值
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
# image.show()
result = tesserocr.image_to_text(image)
print(result)