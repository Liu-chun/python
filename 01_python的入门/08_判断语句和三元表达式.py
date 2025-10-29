# 判断 if 注意写法
a = 3
if a > 5:
    print("条件为真时执行的代码块")
else:
    print("条件为假时执行的代码块")

# 三元表达式
b = 10
c = 20
max = b if b > c else c # 相当于js中 max = b > c ? b : c 如果 b 大于 c 则输出 if 前边的值，否则输出 else 前边的值
print("max =", max)

# if elif else
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')
