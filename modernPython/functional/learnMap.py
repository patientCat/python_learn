from typing import List
"""
在python中练习函数式编程
"""

word_list =["teacher", "incoporate", "render"]

def toUpper(word :str) -> str:
    return word.upper()


## map 返回的是一个map对象，必须使用list将其进行处理
print(list(map(toUpper, word_list)))