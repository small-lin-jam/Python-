import turtle
#begin
r=[]
r5=[]
cs=['red','orange','yellow','green','black','blue','purple']
r1=50
r2=-50
turtle.pensize(10)
#def
def circle(r2):
    turtle.circle(r2,extent=180)
#r-set
for i in range(7):
    r.append(r1)
    r1=r1+10
    r5.append(r2)
    r2=r2-10
#draw
a=0
turtle.lt(90)
for ele in cs:
    turtle.pencolor(ele)
    circle(r[a])
    turtle.rt(180)
    circle(r5[a])
    turtle.rt(180)
    if not (a==6):
        turtle.rt(90)
        turtle.fd(10)
        turtle.lt(90)
    a=a+1