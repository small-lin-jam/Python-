import turtle
turtle.pencolor("black")
turtle.pensize(2)
def printZFX(a):
    turtle.fd(10*a)
    turtle.rt(90)
    turtle.fd(10*a)
    turtle.rt(90)
    turtle.fd(10*a)
    turtle.rt(90)
    turtle.fd(10*a)
for i in range(11):
    printZFX(i)
    turtle.rt(90)