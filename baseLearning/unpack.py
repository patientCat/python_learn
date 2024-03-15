"""
学习python拆包
"""
import random

"""
序列和可迭代对象拆包
"""

"""
1. 元组拆包
"""
name_and_score = ("luke", 89)
name, score = name_and_score
print(f"name={name}, score={score}")

# 假设这是一条数据库记录, 只想取第一个
database_record = ("id", "name", 89, [1, 2, 3, 4])
id, *rest = database_record

print(f"id={id}, rest={rest}")


# 利用* 可以直接拆包
def print_name_and_score(var1, var2):
    print(f"var1={var1}, var2={var2}")


# print_name_and_score(name_and_score) this is wrong without var2
print_name_and_score(*name_and_score)

"""
2. 利用*获取剩余的项
"""

a, b, *rest = range(5)
print(f"a={a}, b={b}, rest={rest}")

"""
for 循环拆包
range for 循环本身就是在拿每个value，自然可以用作拆包
"""

book_list = ["design pattern", "core python learn", "c primer plus"]
for book_name in book_list:
    print(f"book = {book_name}")


# 使用列表推倒式生成
book_price_list = [(x, random.randint(1, 10)) for x in book_list]
for book_name, price in book_price_list:
    print(f"book = {book_name}, price ={price}")
