# 1. 列表 类似数组 <class 'list'>
# li = [1, 2, 3, 4, 5]
# print(li)
# print(type(li))
# 2. 列表的常用方法
# 2.1 列表的索引
li = [10, 20, 30, 40, 50]
# print(li[0])  # 10
# print(li[2])  # 30
# print(li[-1]) # 50 负数索引从末尾开始-1开始
# 2.2 列表的切片 左闭右开 同 字符串切片
# print(li[:3])   # [10, 20, 30]
# 2.3 index 返回元素的索引位置 同字符串的index()
# print(li.index(30))  # 2 
# 2.4 count 统计元素出现的次数 同字符串的count() in not in 
# print(li.count(10))  # 1 in not in
# 2.5 append(value) 在列表末尾添加元素 整体添加到列表中 没有返回值 改变原列表
# li.append(60)
# li.append([60, 70]) # [10, 20, 30, 40, 50, [60, 70]]
# 2.6 extend(iterable) 在列表末尾添加元素 把添加的元素相当于for循环出来依次添加到列表中 没有返回值 改变原列表
# li.extend([70, 80]) # [10, 20, 30, 40, 50, 70, 80]
# 2.7 insert(index, value) 在列表指定索引位置添加元素 原本元素位置的元素后移 改变原列表
# li.insert(2, 25) # [10, 20, 25, 30, 40, 50]
# 2.8 del(index) 删除指定索引位置的元素 改变原列表 不传参数则删除整个列表
# del li[2]
# del li
# 2.9 pop(index) 删除指定索引位置的元素 改变原列表 返回被删除的元素 不传参数则删除末尾元素
# li.pop() # [10, 20, 30, 40]
# li1 = li.pop(2) # 30
# li.pop(1) # [10, 30, 40, 50]
# 2.10 remove(*value) 删除指定元素 改变原列表 找不到元素则报错 返回None
# li.remove(30) # [10, 20, 40, 50]
# li1 = li.remove(40)
# 2.11 clear() 清空列表 改变原列表 返回None
# li.clear() # []
# 2.12 reverse() 反转列表 改变原列表 返回None
# li.reverse() # [50, 40, 30, 20, 10]
# 2.13 sort(key=None, reverse=False) 对列表进行排序 改变原列表 返回None key可选，表示排序规则，reverse可选，表示是否反转排序 默认从小到大排序 只能排序同类型元素
# li.sort() # [10, 20, 30, 40, 50]
# li.sort(reverse=True) # [50, 40, 30, 20, 10]
# 2.14 copy() 复制列表 创建一个新的列表 改变原列表 创建一个新的列表 修改新列表不影响原列表
# li1 = li.copy()
# li1[2] = 99
# print(li1)
# print(li)

# 3. 列表的迭代
# 3.1 方法一
# for i in li:
#   print(i)

# 3.2 方法二
# [print(i) for i in li]

# 3.2 方法三
[print(i) for i in li if i > 20]  # 列表推导式加条件过滤
