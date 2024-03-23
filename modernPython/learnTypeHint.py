
""" 
why we use type hint?

In PEP: the answer is -> to avoid bugs
These annotations can be used to avoid many kind of bugs, for documentation purposes, or maybe even to increase speed of program execution. Here we only focus on avoiding bugs by using a static type checker.
"""

## 基本使用
x : int = 2
y : float = 3.0
varStr : str = "123"

def div(a:int, b:int)->float:
    return a/b

print(div.__annotations__)

# 这里type hint仅仅是提示，对于运行没有任何影响
print(div(2, 3))


## 复杂类型

from typing import List, Tuple, Dict

simpleNames : List = ['lily']
names: List[str] = ['lily', 'tom']
version: Tuple[int, int, int] = (6, 6, 6)
operations: Dict[str, bool] = {'sad': False, 'happy': True}


## Union

from typing import Union
def isNone(x : Union[str, None]):
    if x is None:
        print("x is None")
    else:
        print(f"{str} is not None")


isNone(None)
isNone("luke")

### more readable

from typing import Optional
def isNone(x : Optional[str]):
    if x is None:
        print("x is None")
    else:
        print(f"{x} is not None")

isNone(None)
isNone("luke")

### try 

def isNone(x : Union[str, int, None]):
    if x is None:
        print("x is None")
    else:
        print(f"{x} is not None")


isNone(None)
isNone(12)