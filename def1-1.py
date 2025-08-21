import turtle

turtle.pencolor("black")#set
turtle.pensize(2)#setcolour

#r4
for i in range(4):
    turtle.fd(100) #go100
    turtle.rt(90)#right90
turtle.clear()
#t1
def draw_zfx():
    for i in range(4):
        turtle.fd(100) #go100
        turtle.rt(90)#right90
for i in range(4):
    draw_zfx()
    turtle.rt(90)#right90
turtle.clear()
#t2
for i in range(8):
    draw_zfx()
    turtle.rt(45)