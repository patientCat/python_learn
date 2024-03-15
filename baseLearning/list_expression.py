"""
学习列表推倒式

[expression for item in iterable if condition]

- expression 用于计算变量的值，一个变量或者计算表达式
- item 迭代对象的单个元素
- condition 筛选条件，可选项目
"""

list = range(0, 10)

list_2 = [(x * x) for x in list]
print(list_2)

list_3 = [(x * x) for x in list if x != 3]
print(list_3)

"""
根据当前的了解，python对匿名函数的支持有限，不允许写代码块
expression不能包含分支或者循环（但可以是三目运算语句），也不能包含return或者yield语句。 所谓估值表达式，就是最终能被运算成一个值的表达，例如常量、变量、运算表达式、函数调用、列表切片，等等。
"""

func1 = lambda x: 1 if x == 0 else 2
list_4 = [func1(x) for x in list]
print(list_4)
