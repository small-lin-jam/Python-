import turtle
r=50
r1=-50
for i in range(4):
    turtle.circle(r)
    turtle.rt(90)

turtle.reset()

turtle.rt(90)
turtle.circle(r)
turtle.circle(r1)
turtle.rt(180)
turtle.circle(r,extent=60)
turtle.circle(r1)

turtle.reset()
r=5
for i in range(5):
    turtle.circle(r)
    turtle.fd(100)
    turtle.rt(72)

turtle.reset()
r=50
r1=-50
for i in range(4):
    turtle.circle(r,extent=180)
    turtle.lt(90)
for i in range(4):
    turtle.fd(100)
    turtle.lt(90)