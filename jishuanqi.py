A=input("请选择计算方式（加按1、减按2、乘按3、除按4)")
if (A == '1' ):
    a=int(input("请输入第一个数=")) # int() : 键盘输入字符型 -->整数
    b=int(input("请输入第二个数=")) #
    c=a+b #计算和，赋值给变量c
    print(a,'+',b,'=',c)   #输出结果

elif (A == '2' ):
    a=int(input("请输入第一个数=")) # int() : 键盘输入字符型 -->整数
    b=int(input("请输入第二个数=")) #
    c=a-b #计算差，赋值给变量c
    print(a,'-',b,'=',c)   #输出结果

elif (A == '3' ):
    a=int(input("请输入第一个数=")) # int() : 键盘输入字符型 -->整数
    b=int(input("请输入第二个数=")) #
    c=a*b #计算积，赋值给变量c
    print(a,'*',b,'=',c)   #输出结果
    
elif (A == '4' ):
    a=int(input("请输入第一个数=")) # int() : 键盘输入字符型 -->整数
    b=int(input("请输入第二个数=")) #
    if (b==0):
        print("ERROR")
        c="ERROR"
    else:
        c=a/b #计算商，赋值给变量c
    
    print(a,'/',b,'=',c)   #输出结果