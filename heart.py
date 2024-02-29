import math
from turtle import *
def heartx(k):
    return 15*math.sin(k)**3
def hearty(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(1000)
bgcolor("white")
for i in range(6000):
    goto(heartx(i)*20,hearty(i)*20)
    for j in range(5):
        color("pink")
    goto(0,0)
done()


