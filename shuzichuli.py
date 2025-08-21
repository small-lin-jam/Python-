a=0
b=0
for ele in range(1000,10000):
    a=ele//100
    b=ele%100
    c=(a+b)**2
    if(c==ele):
        print(ele)
    
print('end!')
    