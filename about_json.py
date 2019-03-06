"""
python内置的json模块
json.dumps():将python中的对象转换为Json中的字符串对象
json.loads():将JSON中的字符串对象转换为python中的对象
"""
#  1.把dict转化为json
import json

p_object1 = {'name': '打滑性能', 'age':1}
print("p_object1的类型为%s, 具体为%s" % (type(p_object1), p_object1))
#  把python的dict类型转化为json类型,要输出中文需要指定ensure_ascii参数为False
j_object1 = json.dumps((p_object1), ensure_ascii=False, sort_keys=True)
print("j_object1的类型为%s,具体为%s" % (type(j_object1), j_object1))

#  2.python的class实例对象转化为json
#  直接使用dumps,报错,需要额外知道可选的函数参数
import json


class Man():
    def __init__(self, name, age):
        self.name = name
        self.age = age

man = Man('打滑性能', 1)
json_obj = json.dumps(man, default=lambda obj:obj.__dict__, ensure_ascii=False, sort_keys=True, indent=4)
print(json_obj)