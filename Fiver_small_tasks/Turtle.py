import turtle
import time


# Excerise-1
s = turtle.getscreen()
t = turtle.Turtle()

def excerise1():
    t.forward(100)
    t.left(90)
    t.forward(100)
    time.sleep( 3 )


def excerise2():
    t.fd(100)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(100)
    time.sleep( 3 )



def excerise3():
    t.circle(60)
    time.sleep( 3 )



def excerise4():
    t.shapesize(2,2,2)
    t.fillcolor("red")
    t.begin_fill()
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.end_fill()
    time.sleep(3)


def excerise5():
    t.pen(pencolor="purple", fillcolor="green", pensize=10, speed=15)
    t.begin_fill()
    t.circle(90)
    t.end_fill()
    time.sleep(3)


excerise5()