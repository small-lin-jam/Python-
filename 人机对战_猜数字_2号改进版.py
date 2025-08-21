import time as t
s=100
u_i=0
s = s//2
ss=[]
print("游戏规则：人想数字，如果机器给出的结果大于您写出的数字，请输入“b”如果机器给出的结果小于您写出的数字，请输入“s”；如果机器给出的结果等于您写出的数字，请输入“y”")
print("30秒后开始！")
t.sleep(30)
print("start！")
print("-"*40)
while u_i != "y":
    ss.append(s)
    print("是不是",s,"?")
    u_i=input("请核对您的数字后选择：大（b），小（s），正确（y）！请选择：")
    print("*"*40)
    if u_i == "b":
        s = s//2
        if s==0:
            s=1
    elif u_i == "s":
        s=s+5
        if s >= 100:
            s=100
print("电脑猜测过数字：",ss)
print("电脑猜测次数：",len(ss))
print("THE END!")