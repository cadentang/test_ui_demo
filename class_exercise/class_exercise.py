class Animal:
    '''
    人和狗都是动物，所以创造一个Animal基类
    '''
    # 类属性，类属性可以通过类或者类的实例访问
    # 类属性只能通过类对象来修改，不能通过类的实例来修改
    count = 0
    _aaa = 1
    __bbb = 2

    # 构造函数, 将类实例化
    def __init__(self, name, aggressivity, life_value):
        # 实例属性，实例属性只能通过实例对象来访问和修改，类对象无法修改
        self.__name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    # 实例方法
    # 在类中定义，以self为第一个参数的方法都是实例方法
    # 实例方法在调用时，Python会将调用对象作为self传入
    # 实例方法可以通过实例和类去调用
    # 当通过实例调用时，会自动将当前调用对象作为self传入
    # 当通过类调用时，不会自动传递self，此时我们必须手动传递self
    def eat(self):
        print('%s is eating' % self.name)

    # 类方法
    # 在类内部使用 @classmethod 来修饰的方法属于类方法
    # 类方法的第一个参数是cls，也会被自动传递，cls就是当前的类对象
    # 类方法和实例方法的区别，实例方法的第一个参数是self，而类方法的第一个参数是cls
    # 类方法可以通过类去调用，也可以通过实例调用，没有区别
    @classmethod
    def class_method(cls):
        print("这个是%s的类方法" % cls.name)

    # 静态方法
    # 在类中使用 @staticmethod 来修饰的方法属于静态方法
    # 静态方法不需要指定任何的默认参数，静态方法可以通过类和实例去调用
    # 静态方法，基本上是一个和当前类无关的方法，它只是一个保存到当前类中的函数
    # 静态方法一般都是一些工具方法，和当前类无关
    @staticmethod
    def static_method():
        print("这个是%s的静态方法" %  Animal.__doc__)
        return 1

    # 创建一个可以读但不能修改的属性
    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        return "这个是通过@name.getter方法获取的name，值为%s" % self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("名字必须为字符")
        self.__name = value
        print("这个是通过@name.setter方法重新设置的值，值为%s" % self.__name)

    @name.deleter
    def name(self):
        print("这个是通过@name.deleter方法重新设置的值，值为%s" % self.__name)
        del self.__name

    def __add(self):
        print("这个是双下划线类内部的使用方法")

    def _add(self):
        print("这个是单下划线类内部的使用方法")

class Dog(Animal):
    '''
    狗类，继承Animal类
    '''
    def bite(self, people):

        people.life_value -= self.aggressivity

class Person(Animal):
    '''
    人类，继承Animal
    '''
    person_1 = "aa"

    def __call__(self, *args, **kwargs):
        print("产生人类")

    def __str__(self):
        return "人类：名字%s, 攻击力%s, 生命值%s" % (self.name, self.aggressivity, self.life_value)

    def __setattr__(self, key, value):
        print("执行__setattr__")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        print("执行__getattribute__")
        return super().__getattribute__(item)

    def __delattr__(self, item):
        print("执行__delattr__")

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass

    def __delete__(self, instance):
        pass

    def attack(self, dog):
        dog.life_value -= self.aggressivity



# print(Animal.static_method())
# print(Animal.class_method())
# a = Animal("kitty", 2, 40)
# print(a.property_method)
# print(dir(a))
# print(a.__class__)
# print(a.__dict__)

bb = Person("xianzhang", "100", "1000")
del bb.life_value
# print(bb.life_value)
# bb.person_1 = "bb"
# print(bb.person_1)
#
# Person.person_1 = "dd"
# print(Person.person_1)
# print(bb.person_1)
# print(Person.eat(bb))
# bb.name = "11"
# bb.name
# del bb.name
# print(Animal.__dict__)
# print(Animal.__class__)
# print(a.__class__)
# print(Animal.__name__)
# print(Animal.__doc__)
# print(Animal.__bases__)
# print(Animal.__module__)
# print(Animal.__mro__)
# print(Animal.__qualname__)

