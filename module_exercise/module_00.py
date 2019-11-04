# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:
模块
1.内置模块 os time sys 
2.自定义模块 
3.第三方模块 

模块的搜索路径：
1.程序所在目录
2.环境变量python path
3.标准库路径
4..pth文件自定义路径

模块导入的过程：
1.首先在内存中为每个待导入的模块构建module类的实例：模块对象。这个模块对象目前是空对象，这个对象的名称为全局变量b。
2.构造空模块实例后，将编译、执行模块文件b.py，并按照一定的规则将一些结果放进这个模块对象中。


模块的内置属性：
1. __name__ 当前模块的名字，当作为主程序时值为__main__,当作为被导入的模块时为模块名称
2. __doc__  当前文档的文档说明
3. __file__ 代表当前文件的绝对路径
4.__package__ 文件是否为包
5.__author__ 模块作者信息
6.__all__ 记录包或者模块下那些类、方法及变量对外暴露，对模糊导入才有限制


包: 包含多个python文件的文件夹，且该文件夹下有__init__.py文件

导入的形式：
    1.相对导入
    from .XX import BB
    2.绝对导入
    from XX.BB import CC
    3.可选导入
    try:
        from urlparse import urljoin
        from urllib2 import urlopen
    except ImportError:
        # Python 3
        from urllib.parse import urljoin
        from urllib.request import urlopen
    4.局部导入
    def square_root(a):
        import math
        return math.sqrt(a)
    5.别名

避免导入的方式：
    1.循环导入，A导入B，B导入A
    2.覆盖导入

命名空间：
    如同一个dict，key 是变量名字，value 是变量的值。
    每个函数function 有自己的命名空间，称local namespace，记录函数的变量。
    每个模块module 有自己的命名空间，称global namespace，记录模块的变量，包括functions、classes、导入的modules、module级别的变量和常量。
    build-in命名空间，它包含build-in function和exceptions，可被任意模块访问。
    
    某段Python代码访问 变量x 时，Python会所有的命名空间中查找该变量，顺序是：
    
    local namespace 即当前函数或类方法。若找到，则停止搜索；
    global namespace 即当前模块。若找到，则停止搜索；
    build-in namespace Python会假设变量x是build-in的函数函数或变量。若变量x不是build-in的内置函数或变量，Python将报错NameError。
    对于闭包，若在local namespace找不到该变量，则下一个查找目标是父函数的local namespace。
    
    def func(a=1):
        b = 2
        print(locals())

        return a+b
    func()
    glos = globals()
    glos['d'] = 4
    print(d)
    print(globals())
    
    内置函数locals()、globals()返回一个字典。区别：前者只读、后者可写。
    命名空间 在from module_name import 、import module_name中的体现：from关键词是导入模块或包中的某个部分。
    
    from module_A import X：会将该模块的函数/变量导入到当前模块的命名空间中，无须用module_A.X访问了。
    import module_A：modules_A本身被导入，但保存它原有的命名空间，故得用module_A.X方式访问其函数或变量。
    
直接导入包
https://blog.csdn.net/weixin_38256474/article/details/81228492
"""
# from module_exercise.package01 import *

import sys
# from module_exercise.package01.package01_module00 import aa as A

from module_exercise.package01 import package01_module01 as A



print(A.ClassDD_01)


# print(sys.modules)
# print(package01_module00.__name__)
# print(package01_module00.__doc__)
# print(package01_module00.__file__)
# print(package01_module00.__package__)
# print(package01_module00.__author__)
# print(package01_module00.__all__)
# print(package01_module00)
# print(type(package01_module00))


# def func(a=1):
#     b = 2
#     print(locals())
#
#     return a + b
#
#
# func()
# glos = globals()
# glos['d'] = 4
# print(globals())
#
# from selenium import webdriver