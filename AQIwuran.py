AQI=input("(请输入数字)AQI=")
result=""
AQI=float(AQI)
if (AQI<=50):
    result="一级优"
elif (AQI<=100):
    result="二级良"
elif (AQI<=150):
    result="三级轻度污染"
elif (AQI<=200):
    result="四级中度污染"
elif (AQI<300):
    result="五级重度污染"
else:
    result="六级严重污染"

print("AQI=",AQI,result)

