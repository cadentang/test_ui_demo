#添加了set方法 对比上个代码，；数据描述器
class A:
    def __init__(self):
        self.a1 = 'a1'
        print(2,'A init')
    def __set__(self, instance, value):  #当定义了set魔术方法后，B实例定义的实例属性self.x = 'b1 不会在写进实例字典，而是调用set方法
        print(3,self,instance,value)
        # instance.__dict__['x']=value
    def __get__(self, instance, owner): #return值，将会影响b.x or B.x的调用属性
        print(4,self,instance,owner)
        # return instance.__dict__['x']
        return self


class B:
    x = A()
    def __init__(self):
        print(1,'B init')
        print("+++++++++++++++++++++++")
        self.x = 'b1'
        print("+++++++++++++++++++++++")

b = B()  #output 2->1->+ ->3-> + ；；实例化时候，self.x = 'b1'调用了set方法
print(b.x.a1)  #return a1 直接调用get
# b.x = 100       #return a1 直接调用set
print(b.__dict__)  #实例字典为空
# print(B.__dict__)