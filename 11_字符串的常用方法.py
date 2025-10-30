# 1. find(sub, start, end) 返回字符第一次出现的索引位置，找不到返回-1
a = 'hello world'
print(a.find('o')) # 4 
print(a.find('x')) # -1
print(a.find('ll', 2))

# 2. index(sub, start, end) 跟find()一样，找不到则会报错
print(a.index('o'))

# 3. count(sub, start, end) 返回字符出现的次数
print(a.count('o')) # 2

# 4. len() 返回字符串长度
print(len(a)) # 11

# 5. strip() 去除两边留白
b = '   Jello woEld   '
print(b.strip()) # 'hello world'

# 6. replace(old, new, count) 替换字符串 count可选，表示替换的次数，不写则全部替换
print(a.replace('o', 'x'))
print(a.replace('o', 'x', 1))

# 7. split(sep, maxsplit) 分割字符串，sep可选，表示分割的符号，maxsplit可选，表示最多分割的次数，不写则全部分割 同 js 中的 split 用法一样
print(a.split()) # ['hello', 'world']
print(a.split('l')) # ['he', 'o ', 'wor', 'd']
print(a.split('l', 1)) # ['he', 'o world']

# 8. join(iterable) 将可迭代对象中的元素以字符串连接起来 同 js 中的 join 用法一样
print('-'.join(['hello', 'world'])) # hello-world

# 9. lower() 将字符串转为小写
print(a.lower())

# 10. upper() 将字符串转为大写
print(a.upper())

# 11. islower() 判断是否全部小写
print(a.islower()) # True
print(b.islower()) # False

# 12. isupper() 判断是否全部大写
print(a.isupper()) # False
print(b.isupper()) # False

# 13. startswith(prefix, start, end) 判断字符串是否以prefix开头
print(a.startswith('he')) # True

# 14. endswith(suffix, start, end) 判断字符串是否以suffix结尾
print(a.endswith('ld')) # True

# 15. capitalize() 将字符串的第一个字符转为大写，其他字符转为小写
c = 'hello WORLD'
print(c.capitalize())

# 16. title() 将字符串的每个单词的首字母转为大写，其他字符转为小写
print(c.title())

# 17. isalpha() 判断字符串是否只包含字母
print(a.isalpha()) # True
print(b.isalpha()) # False

# 18. isdigit() 判断字符串是否只包含数字

# 19. isalnum() 判断字符串是否只包含字母和数字

# 20. isspace() 判断字符串是否只包含空格

# 21. zfill(width) 返回一个长度为width的字符串，原字符串右对齐，左边填充0