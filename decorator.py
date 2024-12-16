# 闭包 + 装饰器
def log_decorator(func):
    def inner(*args, **kwargs):
        print("日志信息")
        func(*args, **kwargs)
    return inner
@log_decorator  #fun1 = log_decorator(fun1) 使用装饰器替代这个代码
def fun1():
    print("使用功能1")

@log_decorator #fun2 = log_decorator(fun2)
def fun2(a,b):
    print("使用功能2",a+b)



fun1()
fun2(100,200)