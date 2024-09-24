# 使用海龟绘图编写一个奥运五环(20240925)
from turtle import *
# 第一个圆
width(10)
color("blue")
circle(50)

# 第二个圆
penup()
goto(120,0)
color("black")
pendown()
circle(50)

# 第三个圆
penup()
goto(240,0)
color("red")
pendown()
circle(50)

# 第四个圆
penup()
goto(60,-50)
color("yellow")
pendown()
circle(50)

# 第五个圆
penup() # 抬笔不显示痕迹
goto(180,-50)
color("green")
pendown()# 落笔
circle(50)
done()
