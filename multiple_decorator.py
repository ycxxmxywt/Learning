# 多个装饰器执行顺序
import time


def log(func):
    def inner(*args, **kwargs):
        print("开始执行日志")
        # 执行原有的功能之外，增加功能并不会影响到原有功能
        func()
        print("结束日志")
    return inner

def con_time(func):
    def inner(*args, **kwargs):
        print("开始时间")
        start = time.time()
        # 执行原有的功能之外，增加功能并不会影响到原有功能
        func()
        time.sleep(3)
        end = time.time()
        print("耗时", end - start)
    return inner

def tree(func):
    def inner(*args, **kwargs):
        print("31")
        # 执行原有的功能之外，增加功能并不会影响到原有功能
        func()
        print("32")
    return inner
@log
@con_time # log(con_time(func1))
@tree
# 先定义一个函数
def func1():
    print("这是我定义的函数")

func1()
