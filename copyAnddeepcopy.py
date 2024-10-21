'''
浅拷贝：只拷贝了引用对象过去，复制体和原体共用同一个对象地址
深拷贝：拷贝后，复制体和原体不存在关联关系，编辑等操作时不会影响到原体
'''
import copy

a = [1,2,[5,6]]
c=[1,2,[5,6]]
def copytest():
    b = copy.copy(a)
    print('a',a)
    print("b",b)
    b.append(30)
    b[2].append(7)
    print('浅拷贝之后,修改b')
    print('a',a)
    print("b",b)
    print('*'*30)
copytest()

def copytest():
    b = copy.deepcopy(a)
    print('c',c)
    print("b",b)
    b.append(30)
    b[2].append(7)
    print('深拷贝之后,修改b')
    print('c',c)
    print("b",b)
copytest()