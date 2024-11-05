# 多态
class animal:
    def shout(self):
        print('动物叫了一声')


class dog(animal):
    def shout(self):
        print('狗狗 汪汪叫')


class cat(animal):
    def shout(self):
        print('小猫 喵喵叫')

def animal_shout(a):
    a.shout()

animal_shout(dog())
animal_shout(cat())
animal_shout(animal())