#你想要扩展函数中的某个闭包，允许它能访问和修改函数的内部变量。
def sample():
    n = 0
    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func
import sys
class ClosureInstance:
    def __init__(self,locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        self.__dict__.update((key,value) for key,value in locals.items())
    def __len__(self):
        return self.__dict__['__len__']

def Stack():
    items = []
    def push(item):
        items.append(item)
    def pop():
        return items.pop()
    def __len__():
        return len(items)
    return ClosureInstance()
#actually it is not necessary
# below is the method of timing a function

from timeit import timeit
print(timeit('print(1)',number=1000))
