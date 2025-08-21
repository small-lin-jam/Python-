import random

the_num=random.randint(1,100)

lst_nums=[]

c=200

print('您有',c,'枚硬币')
print('每次猜数将会扣除10枚硬币！加油！')
print('='*30)
while c > 0:
    print('您还有',c,'枚硬币')
    print('='*30)
    u_i=int(input('请输入数据='))
    lst_nums.append(u_i)
    if u_i==the_num:
        print('猜测正确！')
        break
    
    if u_i>the_num:
        print('大了！')
        print('='*30)
        c=c-10
    else:
        print('小了！')
        print('='*30)
        c=c-10
print('='*30)
print('答案=',the_num)
print('剩余硬币=',c)
print('尝试过的数字=',lst_nums)
print('='*30)
