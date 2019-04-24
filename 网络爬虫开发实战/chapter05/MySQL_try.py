# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/24 6:31
# @Author   : tangky
# @Site     : 
# @File     : MySQL_try.py
# @Software : PyCharm

# 使用PyMySQL
# 2.连接数据库
# 创建新数据库spiders
import pymysql

# db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
# connect()方法声明一个MySQL连接对象db,传入host,user,password,port
# print(type(db))
# cursor = db.cursor() # 获取操作游标,来执行SQL语句
# cursor.execute('SELECT VERSION()') # execute执行SQL语句
# data = cursor.fetchone() # 获取第一条数据
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

# 3.创建表
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
# cursor = db.cursor()
# cursor.execute('USE spiders')
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY(id))'
# cursor.execute(sql)
# 4.插入数据
# id = '20120001'
# user = 'Bob'
# age = 20
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# # 动态构造SQL语句,利用字典
# data = {
#     'id': '2012002',
#     'name': 'Ben',
#     'age': 21
# }
# table = 'students'
# keys = ', '.join(data.keys())
# print(keys)
# values = ', '.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# try:
    # cursor.execute(sql, (id, user, age))
#     if cursor.execute(sql, tuple(data.values())):
#         print('Successful')
#         db.commit() # 对于数据插入,更新,删除操作,需要调用commit()方法
# except:
#     print('Failed')
#     db.rollback() # 数据库回滚,无事发生
# db.close()

# 5.更新数据
# import pymysql
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
# cursor = db.cursor()
# cursor.execute('USE spiders')
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#     cursor.execute(sql, (25, 'Bob'))
#     db.commit()
# except:
#     db.rollback()
# db.close()
# # 数据存在,则更新数据;如果数据不存在,则插入数据
# # 使用语句INSERT INTO table(keys) VALUES (values) ON DUPLICATE KEY UPDATE,如果主键已经存在,则执行更新操作
# 6.删除数据:DELETE FROM table WHERE (condition), commit()
# 7.查询数据:SELECT,不需要commit()方法,cursor.rowcount属性获取查询结果的条数,
import pymysql
db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
cursor = db.cursor()
cursor.execute('USE spiders')
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone() # 获取结果的第一条数据,元组
    print('One:', one)
    results = cursor.fetchall() # 获取结果的所有数据,二维元组,但是此时已经提取了第一个数据,指针偏移到第二条数据
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results: # 也可以用while循环加fetchone()方法来获取所有数据,利用了指针会偏移这一点
        print(row)
except:
    print('Error')