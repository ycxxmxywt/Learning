# 通过类封装创建线程
import threading
from time import sleep


class myThread(threading.Thread):#继承线程类
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f'开启{self.name}')
        for i in range(3):
            print(f'{self.name}的第{i}次')
        sleep(3)
        print(f'关闭{self.name}')

if __name__ == '__main__':
    print("开启主线程")
    t1 = myThread('t1') #实例化类
    t2 = myThread('t2')
    t1.start()
    t2.start()
    print("主线程结束")



# 第二种，方法封装创建线程

import threading
from time import sleep


def func1(name):
    print(f"线程{name}开始")
    print(f"线程中间执行的任务")
    sleep(3)
    print(f"线程{name}结束")

if __name__ == '__main__':
    print("主线程")
    # 创建线程
    t1 = threading.Thread(target=func1,args=("t1",))
    t2 = threading.Thread(target=func1, args=("t2",))

    # 执行线程
    print("主线程结束")
    t1.start()
    t2.start()