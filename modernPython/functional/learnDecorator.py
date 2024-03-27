def add_to_string(cls):
    def to_string(self):
        return ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
    cls.to_string = to_string
    return cls

@add_to_string
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(1, 2)

class Test:
    def __init__(self, t) -> None:
        self.t = t
    def func(self):
        print(self.t.to_string())

print(obj.to_string())  # 输出：x=1, y=2
test = Test(obj)
test.func()