import random

the_num=random.randint(1,100)

lst_nums=[]


while True:
    u_i=int(input('请输入数据='))
    lst_nums.append(u_i)
    if u_i==the_num:
        print('猜测正确！')
        break
    if u_i>the_num:
        print('大了！')
    else:
        print('小了！')
print('-'*30)
print('答案=',the_num)
print('猜测次数=',len(lst_nums))
print('尝试过的数字=',lst_nums)
print('-'*30)
