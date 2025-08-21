#最高气温达到35或超过35就称为高温
#获取气温
temperature=float(input('请输入气温'))
#根据不同情况，做出高温判断
if (temperature >=35 ):
    print(temperature,'是高温')
else:
    print(temperature,'不是高温')