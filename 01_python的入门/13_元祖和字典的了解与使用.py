# 1. 元祖 类似列表 但元祖不可变 <class 'tuple'>
# 1.1 元祖的创建
tua = (1, 2, 3, 4, 5)
# tua = (1,) # 如果元祖中只有一个元素，则必须加逗号，否则会被认为是普通括号
# print(type(tua))
# 1.2 元祖的索引 同列表
# print(tua[0])  # 1
# 1.3 元祖的切片 同列表
# print(tua[:3])   # (1, 2, 3)
# 1.4 元祖的遍历 同列表
# for i in tua:
#     print(i)
# 2. 元祖的常用方法
# 2.1 index 返回元素的索引位置 同字符串和列表的index()
# print(tua.index(3))
# 2.2 count 返回元素出现的次数 同字符串和列表的count()
# print(tua.count(3))  # 1

# 2. 字典 类似对象 <class 'dict'>
dic = {
  'name': 'Alice',
  'age': 18,
  'height':1.78
}
# print(dic)
# print(type(dic))
# 2.1 字典的取值
# print(dic['name'])  # Alice
# print(dic.get('age'))  # 18
# 2.2 字典的修改
# dic['name'] = 'Bob'
# dic.update({'age': 20})
# 2.3 字典的添加
# dic['weight'] = 99
# 2.4 字典的删除
# 2.4.1 del 删除指定键值对 改变原字典 不存在则报错 不传参数则删除整个字典
# del dic
# del dic['name']
# 2.4.2 pop(*key) 删除指定键值对 改变原字典 返回被删除的键值对 不存在则报错 不传参数则报错
# dic.pop('name')
# 2.4.3 popitem 删除最后一个键值对 改变原字典 返回被删除的键值对 字典为空则报错
# dic.popitem()
# 2.5 字典的遍历
# for key in dic:
#   print(key, dic[key])
# 2.6 dic 的常用方法
# 2.6.1 keys() 返回字典的所有键
# dict_keys = dic.keys()
# print(dict_keys)
# for key in dict_keys:
#   print(key)
# 2.6.2 values() 返回字典的所有值
# dict_values = dic.values()
# for value in dict_values:
#   print(value)
# 2.6.3 items() 返回字典的所有键值对
# dict_items = dic.items()
# for key, value in dict_items:
#   print(key, value)
# 2.6.4 clear() 清空字典 改变原字典 返回None
# dic.clear()
# 2.6.5 copy() 复制字典 创建一个新的字典 改变原字典 创建一个新的字典 修改新字典不影响原字典
# dic1 = dic.copy()
# dic1['name'] = 'Charlie'
# print(dic1)
print(dic) 
