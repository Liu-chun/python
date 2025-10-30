# 1. 整数类型 
a = 10
a = -10
print('a：', type(a)) # <class 'int'>

# 2. 浮点数类型
b = 3.14
b = -3.14
print('b：', type(b)) # <class 'float'>
# 2.1 科学计数法表示浮点数
b = 1.3e-3
b = 1.8e5
print(b)

# 3.布尔类型 True/False 固定写法
c = True
c = False
print('c：', type(c)) # <class 'bool'>
# 3.1 布尔类型也可以用来表示整数 0/1
# print('c：', True + False)
# print('c：', True + 0)
# print('c：', True + True)
# print('c：', True + 10)

# 4.复数类型 固定写法 j 代表虚数单位 (了解即可)
d = 1 + 2j
print('d：', type(d)) # <class 'complex'>
# 4.1 复数类型的运算方式 实数部分和虚数部分分别运算
# print(2 + 3j + 4 + 5j) # (6+8j)
# print(2 + 3j - (4 + 5j)) # (-2-2j)
# print((2 + 3j) * (4 + 5j)) # (-7+22j) 乘法遵循分配律：(a+bi)(c+di) = (ac-bd) + (ad+bc)i
# print((2 + 3j) / (4 + 5j)) # (0.61+0.04j) 除法遵循有理化原则：(a+bi)/(c+di) = [(a+bi)(c-di)] / ( c^2 + d^2 )

# 5. 字符串类型
e = 'hello'
print('e：', type(e)) # <class 'str'>
# 5.1 多行字符串
e = '''
hello
world
'''
print(e)
# 5.2 字符串的运算
print('hello' + 'world') # helloworld 拼接
print('hello' * 3) # hellohellohello

# 6. 占位符
# 6.1 %s 字符串占位符
name = '张三'
print('我叫%s'  % name)
# 6.2 %d 整数占位符
age = 18
print('我今年%d岁' % age)
# 6.3 %f 浮点数占位符 默认保留6为小数 遵循四舍五入原则
height = 1.78
print('我的身高是%f米' % height) # 我的身高是1.780000米
# 6.4 %.nf 自己定义保留 n 为小数 遵循四舍五入原则
print('我的身高是%.2f米' % height)
# 6.5 多个占位符使用 
print('我叫%s，今年%d岁，身高%.2f米' % (name, age, height))
# 6.6 f-string
print(f'我叫{name}，今年{age}岁，身高{height:.2f}米')