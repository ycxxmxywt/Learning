# 特殊方法add的重载
class Person:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}--{1}".format(self.name ,other.name)
        else:
            return '不是同类'
p1 = Person('构造器的名字')
p2 = Person('其他名字')
print(p1.__add__(p2))
