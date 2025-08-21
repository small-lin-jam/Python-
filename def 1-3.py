import turtle

turtle.pencolor("black")#set
turtle.pensize(2)#setcolour

def a():
    for i in range(3):
        turtle.fd(50) #go100
        turtle.lt(120)#right90

for i in range(5):
    a()
    turtle.fd(50)
    