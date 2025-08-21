a=int(input('请输入购买了几元'))
if a <50:
    b=a
if 50<a<100:
    b=a*0.9
if 100<a:
    b=(a-100)/8+100
    
print('应付款',b) 