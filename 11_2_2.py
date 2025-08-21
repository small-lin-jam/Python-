def isleap(year):
    if year % 100!=0:
        if year % 4 ==0:
            a='ture'
        else:
            a='false'
    else:
        if year % 400 ==0:
            a='ture'
        else:
            a='false'
    return a
l_y=[]
uy=input('year(space,exit)=')
while uy !='':
    uy=int(uy)
    print('saving……',uy)
    l_y.append(uy)
    uy=input('year(space,exit)=')
for i in l_y:
    a=isleap(i)
    print(i,'leap=',a)