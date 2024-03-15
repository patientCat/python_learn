# dict
students = {"luke":1, "james":2}
print(students)

print(students["luke"])

for key in students.keys():
    print(key)


for item in students.items():
    print(item)
    print(item[0])
    print(item[1])

students["new"] = "test"

x = students.pop("not exist", False)
print(x)
