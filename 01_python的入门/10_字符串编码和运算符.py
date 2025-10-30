# 编码格式
# 1. unicode
# 好处：都是2两个字节
# 缺点：占用空间大
# 2.utf-8
# 好处：节省空间
# 缺点：编码格式不同，无法相互转换

# 字符串编码 encode() decode()
a = 'hello world'
b = a.encode()
print(b, type(b)) # b'hello world' <class 'bytes'>
c = b.decode()
print(c, type(c)) # hello world <class 'str'>

d = '你好，世界'
e = d.encode('utf8')
print(e, type(e)) # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c' <class 'bytes'>
f = e.decode()
print(f, type(f)) # 你好，世界 <class 'str'>

# 2字符串运算符
a = 'hello'
b = 'world'
# 2.1 +
print(a + b) # helloworld 拼接
# 2.2 *
print(a * 3) # hellohellohello 复制n次
# 2.3 in
print('h' in a) # True 判断是否存在
print('1' in a) # False
# 2.4 not in
print('h' not in a) # False 判断是否不存在
print('x' not in a) # True
# 2.5 index
print(a[2]) # l 通过索引获取字符，索引从0开始
print(a[-1]) # o 负数索引从末尾开始-1开始
# 2.5 [start:end:step] 切片 左闭右开
str = 'abcdefghij'
print(str[:3]) # abc 从头开始到索引3（不包含3）
print(str[3:8]) # defgh 从索引3开始到索引8（不包含8）
print(str[3:]) # defghij 从索引3开始到末尾
print(str[-3:]) # hij 从倒数第3个开始到末尾
print(str[:-3]) # abcdefg 从头开始到倒数第3个（不包含倒数第3个）
print(str[-1:5:-1]) # jihgf 从末尾开始到索引5（不包含5）逆序
print(str[-1:-3:-1]) # ji 从末尾开始到倒数第3个（不包含倒数第3个）逆序
print(str[::2]) # acegi 步长为2