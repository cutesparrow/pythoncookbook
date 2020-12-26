#你想将一个多层嵌套的序列展开成一个单层列表
from collections.abc import Iterable
items = [1, 2, [3, 4, [5, 6], 7], 8]
def flattern(items,ignoreType=(str,bytes)):
    for i in items:
        if isinstance(i,Iterable) and not isinstance(i,ignoreType):
            yield from flattern(i)
        else:
            yield i
for i in flattern(items):
    print(i)
