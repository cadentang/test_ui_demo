# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:实例属性访问及类描述器：
实例属性访问控制：
    - __getattribute__(self, name)  # 属性、方法拦截器，访问存在的属性或方法时调用（先调用该方法，查看是否存在该属性，
    若不存在，接着去调用__getattr__(self, name)），该方法不要使用这种self.name的形式
    - __getattr__(self, name)  # 访问不存在的属性时调用
    - __setattr__(self, name, value)  # 设置实例对象的一个新的属性时调用，只要是属性被修改或者是赋值，不管这个属性是实例属性、
    类属性、父类的类属性；亦或者是已经存在的属性、不存在的属性，只要是修改和赋值，都会调用到__steattr__方法，该方法里不要对
    属性赋值
    - __delattr__(self, name)  # 删除一个实例对象的属性时调用，使用时不要用del 属性名的形式，只能够删除 已经存在的、实例属性

描述符：
    python描述符是一个“绑定行为”的对象属性，在描述符协议中，它可以通过方法重写属性的访问，如果以下方法任何一个被
    定义在类中，那么这个类就是描述符类，可以规范对所属类的属性访问，即托管属性的作用。
    非数据描述符：只定义了 __get__() /__delete__()方法
    数据描述符：反之,即定义了__set__()方法
    - __get__(self, instance, owner)，用于访问属性。它返回属性的值，或者在所请求的属性不存在的情况下出现 AttributeError 异常
    - __set__(self, instance, value)，将在属性分配操作中调用
    - __delete__(self, instance)，控制删除操作.

实例属性查找优先级（重要）：
    1.__getattribute__()，无条件调用
    2.数据描述符：由 类对象的__getattribute__() 触发调用 （若人为的重载了该 __getattribute__() 方法，可能会导致无法调用描述符）
    3.实例对象的字典（若与描述符对象同名，会被覆盖）
    4.类的字典
    5.非数据描述符
    6.父类的字典
    7.__getattr__() 方法
"""

# 对类属性访问
# class Animal:
#
#     count = 50
#     life = 1000
#
#     def __init__(self, name, aggressivity, life_value):
#         self.count = 0
#         self.__name = name
#         self.aggressivity = aggressivity
#         self.life_value = life_value
#
# black_dog = Animal("xiaohei", 10, 300)
#
# print(Animal.__dict__["count"])  # 获取类对象的count属性
# print(black_dog.__dict__["count"])  # 获取实例对象的count属性
# black_dog.count += 1  # 修改实例对象的count属性
# print(black_dog.count)
# print(Animal.count)
# print(Animal.aaa)
# print(black_dog.aaa)
# print(black_dog.bbb())

aa = 1




# 属性拦截，额外操作
# class Animal:
#
#     count = 50
#     life = 1000
#
#     def __init__(self, name, aggressivity, life_value):
#         self.count = 0
#         self.__name = name
#         self.aggressivity = aggressivity
#         self.life_value = life_value
#
#     def __getattr__(self, name):
#         print('__getattr__')
#
#     def __getattribute__(self, name):
#         print('__getattribute__')
#         return super().__getattribute__(name)
#
#     # def __setattr__(self, name, value):
#     #     print('__setattr__')
#     #     # print(name)
#     #     # print(value)
#
#     def test(self):
#         print("自定义方法")
#
#     # def __delattr__(self, name):
#     #     print('__delattr__')
#
# black_dog = Animal("xiaohei", 10, 300)
# # black_dog.test()
# # print(Animal.__dict__["count"])  # 获取类对象的count属性
# print(black_dog.__dict__)  # 获取实例对象的count属性
# # black_dog.life = 3000
# black_dog.bbb
# # black_dog.test1()
# # black_dog.count += 1  # 修改实例对象的count属性
# # print(black_dog.count)
# # print(black_dog.__dict__)
# # print(Animal.count)
# # print(Animal.life)
# # print(black_dog.life)

bb = 22

# 描述符
class Desc:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        """
        :param self: Desc的实例对象
        :param instance: 描述符所属类的实例对象
        :param owner: 描述符所属的类
        :return:
        """
        print("__get__...")
        print("self.name=", self.name)

    # def __set__(self, instance, value):
    #     self.value = value
    # def update_(self):
    #     pass


class TestDesc:
    x = Desc("x")
    # y = Desc("y")

    def __init__(self, z):
        # self.y = Desc("y")
        self.x = z

# 以下为测试代码
t = TestDesc("33")
# t.x=22
print(t.x)  # 首先调用Owner的__getattribute__() 将t.x转化为TestDesc.__dict__['x'].__get__(None, TestDesc)
# print(t.y)  # 首先调用Owner的__getattribute__() 将t.y转化为TestDesc.__dict__['y'].__get__(t, TestDesc)
# 当Python解释器发现实例对象的字典中，有与描述符同名的属性时，描述符优先，会覆盖掉实例属性。
# 访问实例层次上的描述符x只会返回描述符本身

# def r_test2():
#     r_test1()
#     print("test2")

# r_test1()
#
def r_test1():
    print("test1")



