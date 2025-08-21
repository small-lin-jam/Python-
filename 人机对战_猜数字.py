s=100
u_i=0
s = s//2
ss=[]
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
print("电脑猜测过数字：",ss)
print("电脑猜测次数：",len(ss))
print("THE END!")