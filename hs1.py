#hs1正方形
import turtle

turtle.pencolor("black")
turtle.pensize(2)

for i in range(4):
    turtle.fd(100)
    turtle.rt(90)
    

#hs2田子格
    
def draw_zfx():
    for i in range(4):
        turtle.fd(100)
        turtle.rt(90)

for i in range(4):
    draw_zfx()
    turtle.rt(90)
    
    
#hs3双田字格
for i in range(8):
    draw_zfx()
    turtle.rt(45)