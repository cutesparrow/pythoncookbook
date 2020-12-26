#你想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到。
def increase(n):
    i = n
    while True:
        yield i
        i += 1

c = increase(0)
from itertools import islice
for i in islice(c,20,30):
    print(i)
#islice() 会消耗掉传入的迭代器中的数据。 必须考虑到迭代器是不可逆的这个事实。
