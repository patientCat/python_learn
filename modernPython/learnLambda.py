## 函数的默认值
def funcWithDefaultValue(x, y, value=3):
    print(f"the default value is {value}")


## 可变参数
def processVariableParam(*arg, **kwargs):
    print(f"arg={arg}, kwargs={kwargs}")


processVariableParam(1, 2, 3, name="luke", age=12)

"""
*arg 处理可变参数, 处理位置参数, 按照tuple处理
**kwarg 处理可变参数, 只能处理命名参数, 或者关键字参数, 按照dict处理
"""

def processTuple(a, b, *arg):
    print(arg)
    # *arg 进行拆包
    print(*arg)
    print(sum((a, b, *arg)))

processTuple(1, 2, 3, 4)

def processDict(**kwarg):
    print(kwarg)

processDict(a=1, b=2)


## 装饰器

"""
感觉像是java的切面
"""


def log(x):
    def func(name):
        print("start func")
        name = name.upper()
        x(name)
        print("end func")
    return func

@log
def helloWorld(name):
    print(f"hello name={name} world")

helloWorld("luke")