# 1. int 将其他数据转换为整数 同 js parseInt
# 1.1 浮点数转换为整数小数部分舍去
# num = 1.89 # 1
# num1 = int(num) # 10
# 1.2 字符串转化整数
# num = '10'
# num1 = int(num) # 10
# 1.3 错误转换
# num = '10.89'
# num1 = int(num)
# 1.4 bool转换整数
# num = True
# num1 = int(num)
# print(num1, type(num1))

# 2. float 将其他数据转换为浮点数 同 js parseFloat
# 2.1 字符串转换为浮点数 舍去小数位末尾的 0
# num = '10.89000' # 10.89
# num = '10' # 10.0
# 2.2 bool转换为浮点数
# num = True # 1.0
# num = False # 0.0
# num1 = float(num)
# print(num1, type(num1))

# 3. str 将其他数据转换为字符串 同 js toString 可将任意类型转换为字符串
# 3.1 数字转换为字符串
# st = 10
# st = 10.890 # 10.89
# 3.2 布尔类型转换为字符串
# st = True # True
# 3.3 列表、元祖、字典、集合转换为字符串都是在外层加一个 引号
# st = [1, 2, 3]
# st = (1, 2, 3)
# st = {1, 2, 3}
# st = {'name': '张三', 'age': 18}
# str1 = str(st)
# print(str1, type(str1))

# 4. bool 将其他数据转换为布尔类型 同 js Boolean
# 4.1 0 转换为 False
# bl = 0
# 4.2 非 0 转换为 True
# bl = 10
# bl = [1, 2, 3]
# 4.3 空字符串转换为 False
# bl = ''
# 4.4 空列表、元祖、字典、集合转换为 False
# bl = []
# 4.5 None 转换为 False
# bl = None
# bl1 = bool(bl)
# print(bl1, type(bl1))

# 5. list 将其他数据转换为列表
# 5.1 字符串转换
# li = 'hello world' # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# 5.2 数字类型、布尔类型不可以转换
# 5.3 集合类型转换
# li = {1, 2, 3} # [1, 2, 3]
# 5.4 字典类型转换 只转换键
# li = {'name': '张三', 'age': 18} # ['name', 'age']
# 5.5 元祖类型转换
# li = (1, 2, 3) # [1, 2, 3]
# li1 = list(li)
# print(li1, type(li1))

# 6. tuple 将其他数据转换为元祖 同 list
# 6.1 列表转换
# tup = [1, 2, 3] # (1, 2, 3)
# 6.2 字符串转换
# tup = 'hello world' # ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
# 6.3 集合转换
# tup = {1, 2, 3} # (1, 2, 3)
# 6.4 字典转换
# tup = {'name': '张三', 'age': 18}
# tup1 = tuple(tup.items())
# tup1 = tuple(tup)
# print(tup1, type(tup1))

# 7. set 将其他数据转换为集合 同 list

# 8. dict 将其他数据转换为字典 同 list

# 9. eval 将字符串转换为任意数据 同 js eval
# 9.1 int 字符串转换成整数
# num = '10'
# 9.2 float 字符串转换成浮点数
# num = '10.89'
# 9.3 字符串转换成列表、元祖、字典、集合
# num = '[1, 2, 3]'
# num1 = eval(num)
# print(num1, type(num1))
# 9.4 计算
print(eval('10 + 20'))

