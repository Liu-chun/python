# 1. 作用域 同 js 中的作用域
a = 10 # 全局作用域
# def foo():
#   a = 20 # 局部作用域
#   print(a)
# foo()
# def foo():
#   a = 20
#   print(a) # 20
#   def bar():
#     a = 30
#     print(a) # 30
#   bar()
# foo()
# print(a) # 10

# def foo(a):
#   a = 20
#   print(a) # 20
#   def bar():
#     print(a) # 20
#   bar()
# foo(50)

# 1.2 global 感觉没什么用啊~~~
# def foo():
#   global b # 如果外面已经定义则不会改变外部的值
#   b = 20
#   print(b)
  
# foo()
# print(b) # 20
# def foo():
#   global b, c
#   b = 20
#   c = 30
#   print(b, c)
# foo()
# 1.3 nonlocal 只能在嵌套函数中修改外层函数的变量
# def foo():
#   b = 20
#   print(b)
#   def bar():
#     nonlocal b
#     b = 30
#     print(b)
#     def baz():
#       nonlocal b
#       b = 40
#       print(b)
#     baz()
#   bar()
# foo()

# 2. 匿名函数 lambda
# 2.1 匿名函数的定义 lambda 参数 : 函数体（返回值）
# foo = lambda a, b : a + b
# print(foo(10, 20))
# print((lambda a, b : a + b)(10, 20))
# 2.2 匿名函数的参数
# foo = lambda *args : print(args)
# foo(10, 20, 30)

# foo = lambda **kwargs : print(kwargs)
# foo(a = 10, b = 20)

# 2.3 匿名函数的返回值
# foo = lambda a, b : print(b) if a < b else print(a)
# foo(10, 20)
