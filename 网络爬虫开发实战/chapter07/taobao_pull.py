# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/25 20:58
# @Author   : tangky
# @Site     : 
# @File     : taobao_pull.py
# @Software : PyCharm

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

# options = Options()
# options.add_argument('-headless')
# browser = Firefox(options=options)
browser = Firefox()
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD) # ipad搜索结果页
        browser.get(url) # 跳转
        if page > 1:
            # input.input:nth-child(2)html.ks-gecko66.ks-gecko.ks-firefox66.ks-firefox body.response-wider div#page.srp-page div#main.srp-main div.grid-total div.grid-left div#mainsrp-pager div.m-page.g-clearfix div.wraper div.inner.clearfix div.form input.input.J_Input
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form>input'))) #
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form>span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active>span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


from pyquery import PyQuery as pq


def get_products():
    """
    提取商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


import pymongo

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    :return:
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


MAX_PAGE = 100


def main():
    """
    遍历每一页
    :return:
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)


if __name__ == '__main__':
    browser.get('https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fs.taobao.com%2Fsearch%3Fq%3DiPad')
    browser.find_element_by_xpath('//*[@id="J_Quick2Static"]').click()
    main()
