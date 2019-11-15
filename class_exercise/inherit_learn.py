# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:反射、封装、继承和多态抽象类
反射：
    1.程序可以访问、检测和修改它本身状态或行为的一种能力（自省）
    2.getattr()函数用于返回一个对象的属性值，获取对象object的属性或者方法，存在则返回其属性，不存在则返回默认值，默认值可选
        getattr(object,name[,default])
        object -- 对象
        name   -- 字符串，对象属性
        default-- 默认返回值，如果不提供该参数，在没有对应属性时，将触发AttrbuteError.
        返回值 ：返回对象属性值 
    3.hasattr() 函数用于判断对象是否包含对应的属性
        判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。
        需要注意的是name是一个字符串字面值或字符串类型变量，如果获取的是方法，存在则返回对象中方法的内存地址，
        若想运行则需通过"()"方法.
        hasattr(object,name)
        object -- 对象
        name   -- 字符串，属性名
        返回值 ：如果对象有该属性返回 True，否则返回 False
    4.setattr() 函数对应函数getattr(),用于设置属性值，若属性不存在，则先创建在赋值。
        setattr(object, name, value)
        object -- 对象
        name   -- 字符串，属性名
        value  -- 属性值。
        返回值 ：无
    5.delattr() 函数用来删除指定对象的指定名称的属性，和setattr函数作用相反,属性必须存在，否则发出AttributeError。
        delattr(object, name)

封装：
    1.隐藏对象的属性和实现细节，仅对外提供公共访问方式
    2.私有变量：__变量名
    3.私有方法：__方法名
    
继承：子类拥有父类的所有公有属性和方法
    1.单继承
    2.多继承，继承多个父类
    3.子类对象不能在自己的方法内部，直接访问父类的私有属性或私有方法
    子类对象可以通过父类的公有方法间接访问到私有属性或私有方法
    4.派生：在子类中，添加自己新的属性或者在子类中重新定义这些属性    
    
多态-重写：
    1.多态就是同一个父类的方法，不同子类继承可以进行不同的改写，实现多种不同的功能。(鸭子类型)
    2.在Python中，多态指的是父类的引用指向子类的对象
    3.子类对象可以是父类类型，但是，父类的对象不能是子类类型
    4.不同的子类调用相同的方法，产生不同的结果
    
抽象类：
    抽象类是一个规范，它基本不会实现什么具体的功能，抽象类是不能被实例化
    要想写一个抽象类
        from abc import ABCMeta,abstractmethod
        在这个类创建的时候指定 metaclass = ABCMeta
        在你希望子类实现的方法上加上一个 @abstractmethod装饰器
    使用抽象类
        继承这个类
        必须实现这个类中被@abstractmethod装饰器装饰的方法
"""

# 单继承
class Human:
    """
    父类创建人类
    """
    def __init__(self):
        print('我们都是tester')
        self.life = 0

    def create(self):
        print("人类产生，life=%s", self.life)

    def end(self):
        print("人挂了, end_life=", self.end_life)


class Man(Human):
    """
    男性类
    """
    gender = "man"
    def __init__(self, name):
        print('我是一个帅气的tester')
        super(Man, self).__init__(name)
        self.name = name

    def create(self):
        print("一个男孩产生，life=", self.life)

# h = Human()
# m = Man("小明")
# m.create()
# w = Woman()
# print(isinstance(h,Human))
# print(isinstance(m,Man))
# print(isinstance(m,Human))

qqq=1

# class Human:
#     """
#     父类创建人类
#     """
#     def __init__(self):
#         print('我们都是tester')
#         self.life = 0
#
#     def create(self):
#         print("人类产生，life=%s", self.life)
#
# class Man(Human):
#     """
#     男性类
#     """
#     gender = "man"
#     def __init__(self, name):
#         print('我是一个帅气的tester')
#         super(Man, self).__init__(name)
#         self.name = name
#
#     def create(self):
#         print("一个男孩产生，life=", self.life)
#
#
# class Woman(Human):
#     """
#     女性类
#     """
#     def __init__(self, name):
#         print('我是一个漂亮的tester')
#         super(Woman, self).__init__()
#         self.name = name
#
# class Mid_man(Man, Woman):
#
#     def create(self):
#         print("一个男孩和女孩的产生，life=", self.life)
#
# # # 多继承
# two = Mid_man("AAA")
# two.create()

qqq=2
# 抽象类及多态
# from abc import ABCMeta,abstractmethod
#
# class Payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self):
#         pass
#
#     # @abstractmethod
#     # def shouqian(self):
#     #     pass
#
# class Alipay(Payment):
#     def pay(self,money):
#         print('使用支付宝支付了%s元'%money)
#
# class Wechatpay(Payment):
#     def pay(self,money):
#         print('使用微信支付了%s元'%money)
#
# class ApplePay(Payment):
#     def pay(self,money):
#         print('使用applepay支付了%s元' % money)
#
# def pay(obj,money):
#     obj.pay(money)
#
# p = Payment()
# a = Alipay()
# we = Wechatpay()
# ap = ApplePay()
# pay(a,100)
# pay(we,200)

class BasePage:
    course_a = '//*[@id="9"]'

    def opration(self):
        pass

class CoursePage(BasePage):
    pass

course = CoursePage()
print(course.course_a)
