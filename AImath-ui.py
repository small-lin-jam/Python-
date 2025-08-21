import time as t
import random
lst_nums=[]
s1=100
s2=1
print("请随机一个数字并记下来！")
ui=0
r=0
while ui != "Y":
    if s1>s2:
        r = random.randint(s2,s1)
    if s2>s1:
        r = random.randint(s1,s2)
    t.sleep(0.5)
    print("答案是不是",r,"？")
    lst_nums.append(r)
    ui=input("b为大了，s为小了，Y为正确！请选择：")
    if ui == "s":
        s2=r
    if ui == "b":
        s1=r
    elif ui == "Y":
        break
print('-'*30)
print('答案=',r)
print('机器猜测次数=',len(lst_nums))
print('机器尝试过的数字=',lst_nums)
print('-'*30)

