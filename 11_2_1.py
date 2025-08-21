l_r=[]
l_a=[]
r=input("半径(cm)(space,exit):")
def c_a(r1):
    s=r1*r1*3.14
    return s

while r != '':
    r=float(r)
    print("saving……",r)
    l_r.append(r)
    r=input("半径(cm)(space,exit):")

for r in l_r:
    s=c_a(r)
    l_a.append(s)
print('-'*20)

for i in range(len(l_a)):
    print(l_a[i])
print('-'*20)
print()
print('end!')

