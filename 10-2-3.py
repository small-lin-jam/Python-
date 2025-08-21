import turtle
turtle.pencolor("green")
turtle.pensize(2)
def printZFX(a ):
    turtle.fd(10*a)
    turtle.rt(90)
    turtle.fd(10*a)
    turtle.rt(90)
    turtle.fd(10*a)
    turtle.rt(90)
    turtle.fd(10*a)
for i in range(100):
    printZFX(i)
    turtle.rt(100)