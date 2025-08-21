#根据学生考试分数，转化成对应的等级

mark=float(input('考试分数='))

result="" #等第结束保存变量

if (mark >=90):\
   result="优秀"
elif (mark >=80):
    result="良好"
elif (mark >=60):
    result="合格"
else:
    result="需努力"
    
print(mark,result)