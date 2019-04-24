# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/24 8:16
# @Author   : tangky
# @Site     : 
# @File     : mongo_try.py
# @Software : PyCharm

import pymongo
# client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/') # 直接传入MongoDB的连接字符串
# print(type(client))
# 3.指定数据库
# db = client.test
db = client['test']
# print(db)
# 4.指定集合:MongoDB的每个数据库又包含许多集合(collection),他们类似与关系型数据库中的表
# collection = db.students
collection = db['students']
# print(collection)
# 5.插入数据:调用insert()方法返回_id值
# 对于students这个集合,新建一条学生数据,这条数据以字典形式表示
# student = {
#     'id': '20170102',
#     'name': 'Westbrook',
#     'age': 29,
#     'gender': 'male'
# }
# result = collection.insert_one(student) # 返回InsertOneResult对象,inserted_id属性获取_id
# student1 = {
#     'id': '20170103',
#     'name': 'Adams',
#     'age': 25,
#     'gender': 'male'
# }
# student2 = {
#     'id': '20170104',
#     'name': 'Steve',
#     'age': 25,
#     'gender': 'male'
# }
# result = collection.insert_many([student1, student2])
# print(result) # InsertManyResult对象
# print(result.inserted_ids) # inserted_ids属性获取_id列表
# 6.查询,find_one()返回单个结果或find()方法返回一个生成器对象进行查询,
# result = collection.find_one({'name': 'Adams'})
# print(type(result)) # 返回一个字典
# print(result) # 其中的_id属性,这就是MongoDB在插入过程中自动添加的
# # 也可以根据ObjectId来查询,此时需要使用bson库里面的objectid:
# from bson.objectid import ObjectId
# result = collection.find_one({'_id': ObjectId('5cc01b8552ad20dc7328e74e')})
# print(result) # 查询结果依然是字典类型,如果不存在返回None
# # 对于多条数据,使用find()方法
# results = collection.find({'age': 25})
# print(results) # 返回Cursor类型,相当于一个生成器
# for result in results:
#     print(result) # 返回的结果是字典类型
# # 查询年龄大于20的数据,$gt,greater than
# results = collection.find({'age': {'$gt': 20}})
# print(results)
# for result in results:
#     print(result)
# # 正则匹配查询:例:{'name': {'$regex': '.*'}}还有另外的功能符号
# results = collection.find({'name': {'$regex': '.*e.*'}})
# print(results)
# for result in results:
#     print(result)
# 7.计数:统计查询结果由多少条数据,可以调用count()方法
# count = collection.find().count() # count()方法快过时了
# count = collection.count_documents({'age': 25}) # 统计年龄为25的数据条数
# print(count)
# print(type(count)) # int类型
# 8.排序:sort()方法,在其中传入排序的字段及升降序标志即可.
# results = collection.find().sort('name', pymongo.ASCENDING) # 按name升序(pymongo.ASCENDING)
# results = collection.find().sort('age', pymongo.DESCENDING)
# print([result['name'] for result in results])
# 9.偏移:只取某几个元素,利用skip()方法偏移几个位置,比如偏移2,就忽略前两个元素,得到第三个及以后的元素
# results = collection.find().sort('name', pymongo.DESCENDING).skip(2)
# print([result['name'] for result in results])
# # limit()方法指定要取的结果个数
# results = collection.find().sort('name', pymongo.DESCENDING).skip(2).limit(2) # limit(2)只返回两个结果
# print([result['name'] for result in results])
# # 值得注意的是,在数据库数量非常庞大时,最好不要使用大的偏移量来查询数据,因为这样可能导致内存溢出.可使用类似以下操作
# from bson.objectid import ObjectId
# results = collection.find({'_id': {'$gt': ObjectId('5cc01b8552ad20dc7328e74e')}})
# print([result['name'] for result in results])
# 10.更新:使用update()方法,!!不推荐,指定更新的条件和更新后的数据即可
# # 使用update_one(),update_many()方法,第二个参数需要使用$类型操作符作为字典的键名
# condition = {'name': 'Adams'}
# student = collection.find_one(condition)
# student['age'] = 28
# result = collection.update_one(condition, {'$set': student})
# print(result) # UpdateResult类型
# print(result.matched_count, result.modified_count) # 匹配的数据条数和影响的数据条数
# condition = {'age': {'$gt': 20}}
# result = collection.update_one(condition, {'$inc': {'age': 1}}) # 执行之后会将第一条符合的数据年龄加1
# print(result)
# print(result.matched_count, result.modified_count)
# # update_many()方法,将所有符合条件的数据都更新
# condition = {'age': {'$gt': 20}}
# 11.删除: