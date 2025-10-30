# 算数运算符 
# + - * / % ** //
a = 10
b = 2
print(a / b) # 5.0 除法 永远返回浮点数
print(a // b) # 5 整除 返回整数部分，舍弃小数部分
print(a ** b) # 幂运算 运算符优先级高于算数运算符

# 赋值运算符 
# = += -= *= /= %= **= //=

# 转义
# \n 换行 \t 制表符 \\ 反斜杠 \' 单引号 \" 双引号 \r 回车舍弃前面内容
print('hello\nworld')
print('hello\tworld')
print('hello\\world')
print('hello\'world')
print('hello\"world')
print('hello\rworld')
# r 原生字符串 不进行转义
print(r'hello\nworld')

# 关系运算符
# > < >= <= == !=
age = int(input("请输入你的年龄："))
if age >= 18:
    print('你已成年')
else:
    print('你未成年')
    
# 逻辑运算符
# and or not 与 js 逻辑一样写法不同

