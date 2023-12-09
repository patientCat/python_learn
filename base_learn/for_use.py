# 学习for
for i in range(1, 11):
    print(i, end = '\t' )
print()

for i in range(0, 10, 3):
    print(i, end = '\t' )
print()

my_books = ['linux', 'redis', 'cpp']

print("use index for")
for i in range(0, len(my_books)):
    print(my_books[i])

print("use range for")
for value in my_books:
    print(value)

"""
测试拆包逻辑理解
"""
print("use first letter")
for letter,*rest in my_books:
    print(letter)
    print(rest)
