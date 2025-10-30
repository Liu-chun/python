# 1. while 循环
i = 0
# while i < 5:
#   print(i)
#   i += 1
# sum = 0
# while i <= 100:
#   sum += i
#   i += 1
# print("1-100的和为：", sum)

# 1.1 while 嵌套
while i < 5:
  print(f'外层循环{i}')
  j = 0
  while j < 4:
    print(f'内层循环{j}')
    j += 1
  i += 1
  
# 2. for 循环 range(start, stop, step) 左闭右开 和js中的 for in 一样 都是可迭代对象
for i in range(1, 4):
  print(i) # 1 2 3
  for j in range(3):
    print(j)

# continue break 同 js 用法一样