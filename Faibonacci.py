n = int(input("n="))
a=0
b=1
c=0
print("0",end='\t')
for i in range(n+1):
    c=a+b
    a=b
    b=c
    print(c,end='\t')
print()
print("-"*40)
print("end")