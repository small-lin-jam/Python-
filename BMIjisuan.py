kg=float(input('请输入你的体重(kg)'))
cm=float(input('请输入你的身高（cm）'))
m=cm / 100
BMI=(kg / m**2)
if BMI <=17 :
    result='体重过轻'
elif 18.5 <= BMI <24 :
    result='正常'
elif 24 <= BMI <27 :
    result='过重'
elif 27 <= BMI <30 :
    result='轻度肥胖'
elif 30 <= BMI <35 :
    result='中度肥胖'
else :
    result='重度肥胖'

print(result)