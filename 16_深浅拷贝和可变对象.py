# 深浅拷贝没什么说的，用js用法一样
# 1. 浅拷贝 copy() 同 js 的浅拷贝
# a = [1, 2, 3, [4, 5, 7], 5]
# b = a.copy()
# # b[0] = 0
# # 深拷贝 deepcopy() 同 js 的深拷贝
# import copy 
# c = copy.deepcopy(a)
# print(a, b) 

# 2. 可变对象 直接修改内存地址不会改变
# 2.1 列表
# a = [1, 2, 3, 4, 5]
# print(a,  id(a))
# a[0] = 0
# print(a,  id(a))
# 2.2 字典
# a = {'name': 'Alice', 'age': 18}
# print(a,  id(a))
# a['name'] = 'Bob'
# print(a,  id(a))
# 2.3 集合
# a = {1, 2, 3, 4, 5}
# print(a,  id(a))
# a.add(6)
# print(a,  id(a))

# 3. 不可变对象 基本数据类型 修改内存地址会改变
# 3.1 整数
# 3.2 字符串
# 3.3 元组
# ...
