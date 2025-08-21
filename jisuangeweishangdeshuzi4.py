#计算获得a的各个位上的数字
a =int(input('请输入一个四位数'))
#个位
result=a % 10
print(result)
#十位
a=a // 10
result=a % 10
print(result)
#百位
a=a // 10
result=a % 10
print(result)
#千位
a=a // 10
result=a % 10
print(result)