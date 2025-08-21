import random

the_num = random.randint(1,100)
list_nums = []
user_input=0
while user_input != the_num:
    user_input = int(input('请输入数字：'))
    list_nums.append(user_input)
    if user_input==the_num:
        print('猜测正确!')
    if user_input>the_num:
        print('大了!') 
    else:
        print('小了!')
print('-'*30)
print('电脑数字:',the_num)
print('猜测次数:',len(list_nums))
print('猜测数字:',list_nums)
print('-'*30)