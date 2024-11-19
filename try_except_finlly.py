# 抛出异常练习及with方法管理文件资源

# 第一种
try:
    f = open("C:/Users/dell/Downloads/测试.txt",'r',encoding='utf-8')
    for line in f.readlines():
        print(line)
except BaseException as e:
    print('有异常')
    print(e)
finally:
    print('关闭文件')
    f.close()

# 第二种
with open('C:/Users/dell/Downloads/测试.txt','r',encoding='utf') as f:
    for line in f:
        print(line)
