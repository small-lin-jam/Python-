import turtle
def draw_wjx(pos=(-165,45),length=330):
    # 到 pos 位置
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()

    turtle.begin_fill()
    turtle.fillcolor('yellow')

    for i in range(5):
        turtle.fd(length)
        turtle.right(144)
    
    turtle.end_fill()
#background
turtle.pencolor('red')
turtle.pensize(1000000)
turtle.fd(100)
turtle.lt(180)
turtle.fd(100)
turtle.rt(90)
turtle.fd(200)
turtle.rt(90)
#circle
turtle.pencolor('yellow')
turtle.pensize(50)
turtle.circle(-200)
#fivejiao
turtle.pensize(1)
draw_wjx(pos=(-165,45),length=330)
