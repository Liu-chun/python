# 1. 函数 同 js 函数
# def foo() :
#   print('hello world')
# foo()

# 2. 参数
# def sum(num1, num2):
#   return num1 + num2
# total = sum(10, 20)
# print(total)
# 2.1 默认参数 默认参数必须放在普通参数后面
# def sum(num1, num2 = 10):
#   return num1 + num2
# print(sum(10))
# 2.3 可变参数 类 js ...args 但是返回的是元祖类型
# def bar(*agrs):
#   print(agrs)
#   print(type(agrs))
# bar({'name': '张三', 'age': 18})
# 2.4 关键字参数 只接受字典 类 js ...args 但是返回的是字典类型
# def bar(**kwargs):
#   print(kwargs)
#   print(type(kwargs))
# bar(name = '张三', age = 18)
# 2.5 多个返回值 返回一个元祖
def sum(num1, num2):
  return num1 + num2, num1 - num2
total, sub = sum(10, 20)

# 3. 函数的嵌套
def foo():
  print('hello', end=' ')
  def bar():
    print('world')
  bar()
foo()