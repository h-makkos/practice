#实验三.使用蒙特.卡罗方法计算圆周率近似值
from random import random
times=int(input('Please input:'))
hit=0
for i in range(times):
    x=random()
    y=random()
    if x*x+y*y<=1:
        hit+=1
p=hit/times
print(p*4)
