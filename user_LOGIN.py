#user_LOGIN.py
import random
import time as t
'''
this code is written by Steven Lin(Lin Junhui)
copyright (c) Steven Lin Studio
Tips：
adminNO.:0
adminname:Steven
adminpassword:2798@Steven
admintest:
admintestNO.:1
name:admintest
password:279800
errcodes:
0x00001:由于等级设置为"拒绝访问"或"阻止授权"或"临时人员"或"敌对人员"，系统拒绝访问
0x00002:由于等级设置为"阻止授权"或"敌对人员"，系统拒绝授权为普通用户
0x00003:无法删除管理员
0x00004:由于管理员操作，账号不存在(搜索失败)
0x00005:迷你游戏不存在(搜索失败)
'''
#初始化
l=[['Steven','279800','管理员'],['admintest','279800','管理员']]
ln=[0,1]
a=1
np=[]
ld=[]
#E.S.S
def ESS(name):
    print('From System To',name,':you are now in the error search system(E.S.S),this system is all English')
    c=input('errorcode:')
    if c=='0x00001':
        print('you have searched:',c)
        print('errorname:由于等级设置为"拒绝访问"或"阻止授权"或"临时人员"或"敌对人员"，系统拒绝访问')
    if c=='0x00002':
        print('you have searched:',c)
        print('errorname:由于等级设置为"阻止授权"或"敌对人员"，系统拒绝授权为普通用户')
    if c=='0x00003':
        print('you have searched:',c)
        print('errorname:无法删除管理员')
    if c=='0x00004':
        print('you have searched:',c)
        print('errorname:由于管理员操作，账号不存在(搜索失败)')
    if c=='0x00005':
        print('you have searched:',c)
        print('errorname:迷你游戏不存在(搜索失败)')
    print('From System To',name,':you are now in the user login system(U.L.S)')
def minigame1(name):
    print('欢迎来到minigame1——猜数字！',name,'！')
    the_num = random.randint(1,100)
    user_input=0
    list_nums = []
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
#阻止退出
while True:
    #输入信息
    c=0
    print()
    print('欢迎使用账号登录系统(U.L.S)！')
    print('='*30)
    b=int(input('编号（从2开始）：'))
    n=input('姓名：')
    p=input('密码：')
    print("查询中……")
    t.sleep(3)
    for ele in ld:
        if c==ele:
            print('systemerror:0x00004')
            print('errorname:userremoved(search failed)')
    for ele in ln:
        c=int(b)
        if ele == b:
            print('查询成功！')
            #管理员信息比较
            if n == l[0][0]:
                if p == l[0][1]:
                    print("欢迎！",l[0][0],"等级：",l[0][2],"!")
                    while c != "x":
                        print("添加信息请按1，删除信息请按2，读取信息请按3，错误代码查询请按S，退出请输入x")
                        c=input('请输入选择：')
                        if c=="1":
                            user=input('请输入用户名：')
                            np.append(user)
                            user=input('请输入密码：')
                            np.append(user)
                            user=input('请输入等级：')
                            np.append(user)
                            print('保存中……')
                            l.append(np)
                            a=a+1
                            print('您的编号为：',a)
                            ln.append(a)
                            print('保存成功！')
                        if c=="2":
                            c=input('被删除者编号：')
                            if c != "0" or c != "1":
                                print('删除中……')
                                l[c].clear()
                                c=int(c)
                                ld.append(c)
                                print('删除完成！')
                            else:
                                print('systemerror:0x00003')
                                print('errorname=systemcannotremoveadmin')
                                print('please try again!')
                        if c=="3":
                            print("目前信息：")
                            b=0
                            for i in l:
                                print("编号：",b,"用户名、密码及等级：",i)
                                b=b+1
                        print('='*30)
                        if c=="S" or c=="s":
                            ESS(n)
                else:
                    print('管理密码错误！')
            #用户信息比较
            else:
                n1=l[b][0]
                p1=l[b][1]
                if n == n1:
                    if p == p1:
                        print('='*30)
                        print('欢迎！',l[b][0],"等级：",l[b][2],"!")
                        while c != "x":
                            print('更改信息请按1，更改等级为正式人员请按2，玩迷你游戏请按3，查询错误代码请按S，退出请输入x')
                            c=input('请输入选择：')
                            if c == "1":
                                print('您的编号为：',b,'请您牢记！')
                                if l[b][2]=="阻止授权" or l[b][2]=="拒绝访问" or l[b][2]=="临时人员" or l[b][2]=="敌对人员":
                                    print('systemerror:0x00001')
                                    print('errorname=adminrefuse')
                                    print('please call the admin to repair your level!')
                                else:
                                    rn=input('更改后的名称：')
                                    rp=input('更改后的密码：')
                                    l[b][0]=rn
                                    l[b][1]=rp
                            if c == "2":
                                if l[b][2]=="阻止授权" or l[b][2]=="敌对人员":
                                    print('systemerror:0x00002')
                                    print('errorname=systemrefuse')
                                    print('please call the admin to repair your level!')
                                else:
                                    l[b][2]="正式用户"
                                    print('授权成功！')
                            if c == "3":
                                if l[b][2]=="阻止授权" or l[b][2]=="敌对人员":
                                    print('systemerror:0x00002')
                                    print('errorname=systemrefuse')
                                    print('please call the admin to repair your level!')
                                else:
                                    c=input("请输入迷你游戏编号：")
                                    if c=="1":
                                        minigame1(n)
                                    else:
                                        print('systemerror:0x00005')
                                        print('errorname=systemcannotsearchminigamewhichcodeis',c)
                                        print('please try again!')
                            if c=="S" or c=="s":
                                ESS(n)
                            print('='*30)
                    else:
                        print('验证失败！')
                else:
                        print('验证失败！')
            print('='*30)
'''
code is now end
written by Steven Lin(Lin Junhui)
'''