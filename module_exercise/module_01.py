# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:
模块
1.内置模块
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
3.

模块的内置属性：
1. __name__ 当前模块的名字，当作为主程序时值为__main__,当作为被导入的模块时为模块名称
2. __doc__  当前文档的文档说明
3. __file__ 代表当前文件的绝对路径
4.__package__ 文件是否为包
5.__author__ 模块作者信息
6.__all__ 记录包或者模块下那些类、方法及变量对外暴露，对模糊导入才有限制



包: 包含多个python文件的文件夹，且该文件夹下有__init__.py文件
__init__.py文件的作用：

"""
# from module_exercise.package01 import *
from module_00 import *

print(package01_module00.__doc__)
print(package01_module00.__file__)
print(package01_module00.__package__)
print(package01_module00)
print(type(package01_module00))