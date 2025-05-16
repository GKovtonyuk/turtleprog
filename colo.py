import random
from turtle import*
colors=["red","blue"]
def circleMy(r,x,y):
    up()
    goto(x,y)
    down()
    color(random.choice(colors))
    circle(r)
    up()
    
circleMy(30,0,0)
circleMy(60,70,60)
circleMy(100,200,100)
done()
