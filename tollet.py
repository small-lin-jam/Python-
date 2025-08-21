#tollet
import turtle as t
import tools as ts
print('begin to draw tollet')
t.pu()
t.speed(9999999999999)
t.screensize(200,200)

#begin
    #man
    #head
t.pu()
t.pensize(1)
t.begin_fill()
t.fillcolor('black')
ts.dcircle(cx=-125,cy=95,lenth=-30,h=365,fc='black')
t.end_fill()
    #body
t.pu()
t.goto(-100,25)
t.pd()
t.begin_fill()
t.fillcolor('black')
t.pensize(25)
ts.dmt(x=-158,y=25,l1=15,l2=200,h=0,fc='black')
ts.dmt(x=-108,y=25,l1=15,l2=200,h=0,fc='black')
ts.dmt(x=-158,y=25,l1=50,l2=100,h=0,fc='black')
t.pensize(15)
ts.dmt(x=-190,y=25,l1=10,l2=75,h=0,fc='black')
ts.dmt(x=-70,y=25,l1=10,l2=75,h=0,fc='black')
#|
t.pensize(15)
ts.dl(cx=0,cy=0,l=400,h=-90)
#woman
    #head
t.pu()
t.pensize(1)
t.goto(-95,125)
t.begin_fill()
t.fillcolor('black')
ts.dcircle(cx=140,cy=95,lenth=-30,h=365,fc='black')
t.end_fill()
    #body
t.pu()
t.goto(100,25)
t.pd()
t.begin_fill()
t.fillcolor('black')
t.pensize(25)
ts.dmt(x=158,y=25,l1=15,l2=200,h=0,fc='black')
ts.dmt(x=108,y=25,l1=15,l2=200,h=0,fc='black')
ts.dmt(x=108,y=25,l1=50,l2=100,h=0,fc='black')
t.pensize(15)
ts.dmt(x=195,y=25,l1=10,l2=75,h=0,fc='black')
ts.dmt(x=75,y=25,l1=10,l2=75,h=0,fc='black')
    #dress
ts.ds(x=140,y=-100,l=135,h=0,fc='black')
#text
t.pu()
t.goto(-150,250)
t.pd()
t.write('预备（11）班 林俊辉 03号',font=("Arial", 20, "normal"))
print('end to draw tollet')