#nn,pddi
input=int(input('请输入需要几次方数？（禁止1或0）'))
if (input==1) or (input==0):
    print('error')
else:
    for ele in range(100,1000):
        a=ele//100
        b=ele%100//10
        c=ele%10
        if (a**input+b**input+c**input==ele):
            print(ele)
print('-'*40)
print('END')