with open('/etc/passwd') as f:
    for i in f:
        print(i,end='')
from itertools import dropwhile
with open('/etc/passwd') as f:
    for i in dropwhile(lambda line: not line.startswith('#'),f):
        print(i,end='')

items = ['a', 'b', 'c', 1, 4, 10, 15]
from itertools import islice
for i in islice(items,3,None):
    print(i)

#跳过一个可迭代对象的开始部分跟通常的过滤是不同的,we don't need do any checkafter finding a valid item

