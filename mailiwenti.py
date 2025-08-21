#mlwt

num=int(input('格子数='))
s=0#mlzh
p=1#mls

for i in range(num+1):
    s=s+p
    p=p*2

print('小麦粒=',s)

t=150000*0.76/1000  # T 计算

print('吨数=',t)