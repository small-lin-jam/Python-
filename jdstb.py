#输入
hand1=input('hand1=剪刀a，石头b，布c：')
hand2=input('hand2=剪刀a，石头b，布c：')
#结果1
if (hand1=='a') and (hand2=='a'):
    print('平局！')
elif (hand1=='b') and (hand2=='b'):
    print('平局！')
elif (hand1=='c') and (hand2=='c'):
    print('平局！')
#结果2
elif (hand1=='c') and (hand2=='b'):
    print('hand2获胜！')
elif (hand1=='a') and (hand2=='b'):
    print('hand2获胜！')
elif (hand1=='c') and (hand2=='a'):
    print('hand2获胜！')
elif (hand1=='c') and (hand2=='b'):
    print('hand2获胜！')
#结果3
elif (hand1=='a') and (hand2=='c'):
    print('hand1获胜！')
elif (hand1=='b') and (hand2=='a'):
    print('hand1获胜！')
elif (hand1=='a') and (hand2=='c'):
    print('hand1获胜！')
elif (hand1=='b') and (hand2=='c'):
    print('hand1获胜！')
else:
    print('ERROR')