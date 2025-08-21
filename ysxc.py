n=int(input('n='))
print('n=',end='/t')
while (n!=0):
    if (n%7==0):
        print('7*',end='/t')
        a=7
    elif (n%5==0):
        print('5*',end='/t')
        a=5
    elif (n%3==0):
        print('3*',end='/t')
        a=3
    elif (n%2==0):
        print('2*',end='/t')
        a=2
    else:
        n=n-1
        print
        print('-'*40)
    n=n//a
print('end!')