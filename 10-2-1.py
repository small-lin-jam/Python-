#print 1-100
a=int(input('请输入倍数:'))
def printZC():
    print('-'*30)
    for i in range(1,101):
        if i % a==0:
            print(i,end='     ')
    print()
    print('-'*30)
printZC(a)