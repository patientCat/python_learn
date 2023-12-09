# 学习字符串，明白字符串不可变
def learn_str_is_immuatable():
    str1 = "a"
    str3 = str1 + "b"
    print(str1)
    print(str3)

def learn_str_contains():
    if "ll" not in "hello":
        print("yes")
    else:
        print("no")

def learn_str_format():
    x = "luke"
    print(f"{x} is good")

learn_str_format()
