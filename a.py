import math
from turtle import *
def hearta(a):
    return 15*math.sin(a)**3
def heartb(a):
    return 12*math.cos(a)-5*\
            math.cos(2*a)-2*\
            math.cos(3*a)-\
            math.cos(4*a)

speed(1000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20, heartb(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)
penup()
goto(0, -50)  
pendown()
color("white")  
write("Hồng Mai", align="center", font=("Arial", 18, "normal"))
done()