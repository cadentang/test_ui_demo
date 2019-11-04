"""
description:这个文件是测试登录的脚本集合
"""
__author__ = "caden"
__all__ = ["ClassCC"]
aa = "asas"

# def test_1():
#     pass

class ClassCC:
    pass

# from module_exercise.package01.package01_module01 import *
# from module_exercise.package01.package01_module01 import ClassDD_00, ClassDD_01  # 尽量是具体导入，不要模糊导入
#
# from module_exercise.package01 import package01_module01
# from module_exercise import package01
# from module_exercise import package01.package01_module01 # 语法错误
# from module_exercise import package01 # 不建议这样
print(__author__)

# print(package01.package01_module00.ClassDD_01)
# print(package01_module01.ClassDD_01)


from module_exercise.package01.package01_module01 import *

print(ClassDD_00)

