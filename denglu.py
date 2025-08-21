#1,用户输入，分别保存变量为（accout,password）
a=input('用户名=')
p=input('密码=')
print('-'*40)
#2,检验
if (a=='12345') and (p==('00000')):
    print(a,p)
    print('欢迎')
else:
    print('密码或帐号名错误！')