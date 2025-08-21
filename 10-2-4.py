import turtle
a=int(input('个数:'))
turtle.pencolor("green")
turtle.pensize(2)
turtle.lt(30)
def printZFX(a):
    turtle.fd(100)
    turtle.rt(120)
    turtle.fd(100)
    turtle.rt(60)
    turtle.fd(100)
    turtle.rt(120)
    turtle.fd(100)
    turtle.rt(60)
for i in range(a):
    printZFX(i)
    turtle.rt(160)