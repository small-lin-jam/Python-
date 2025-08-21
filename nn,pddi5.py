#nn,pddi
input=int(input('请输入需要几次方数？（禁止1或0）'))
if (input==1) or (input==0):
    print('error')
else:
    for ele in range(1000,10000):
        a=ele//1000
        b=ele%1000//100
        c=ele%100//10
        d=ele%10
        if (a**input+b**input+c**input+d**input==ele):
            print(ele)
print('-'*40)
print('END')