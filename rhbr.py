#输入年份
nian=int(input('请输入当前年份'))
yn=nian % 400
a=nian
if (yn==0):
    rhbr=nian /400
    print('是世纪闰年！')
elif (yn!=0):
    if (nian % 4 !=0) :
        print('不是闰年！')
    else:
        print('是闰年！')
