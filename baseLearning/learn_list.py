# learn_list
test_list = [x for x in range(1, 10)]

print(test_list)

# 这里拿到的是复制，而不是引用
slice1 = test_list[1:3]
print(slice1)

slice1.append(3)

print(slice1)
print(test_list)

# 更好地处理for循环
list_of_tuple = [("book", 3), ("pencil", 10)]

for key, value in list_of_tuple:
    print(key)
    print(value)

list_of_tuple = [["book", "pencil"], [1, 2]]

for key, value in list_of_tuple:
    print(key)
    print(value)

students = ["luke", "james"]
student_pre = ["pre" + stu for stu in students]
print(student_pre)
