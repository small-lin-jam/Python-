import turtle

tl = turtle.Turtle()


# 画外框
def draw_border(pos=(-300,200),width=600,height=400):
    tl.penup()
    tl.goto(pos)
    tl.pendown()
    tl.begin_fill()
    tl.fillcolor('red')
    for i in range(2):
        tl.fd(width)
        tl.right(90)
        tl.fd(height)
        tl.right(90)
    
    tl.end_fill()


# 到某个位置，画五角星
def draw_wjx(pos=(0,0),length=90):
    # 到 pos 位置
    tl.penup()
    tl.goto(pos)
    tl.pendown()

    tl.begin_fill()
    tl.fillcolor('yellow')

    for i in range(5):
        tl.fd(length)
        tl.right(144)
    
    tl.end_fill()


 
# tl.pencolor("red")

def flag_ch():
    tl.pencolor("red")
    draw_border()
    tl.pencolor('yellow')
    draw_wjx(pos=(-275,115),length=90)

    tl.setheading(25)
    draw_wjx(pos=(-175,160),length=30)

    # tl.setheading(25)

    draw_wjx(pos=(-135,120),length=30)

    tl.setheading(-25)
    draw_wjx(pos=(-140,70),length=30)

    draw_wjx(pos=(-175,20),length=30)
    
    #tl.hideturtle()
    
def some_stars():
    draw_border()
    tl.pencolor('yellow')
    
    
    draw_wjx(pos=(-150,100),length=60)
    draw_wjx(pos=(-150,0),length=60)
    draw_wjx(pos=(-150,-100),length=60)

    draw_wjx(pos=(0,100),length=60)
    draw_wjx(pos=(0,0),length=60)
    draw_wjx(pos=(0,-100),length=60)
    
    draw_wjx(pos=(150,100),length=60)
    draw_wjx(pos=(150,0),length=60)
    draw_wjx(pos=(150,-100),length=60)
    
draw_border()
flag_ch()