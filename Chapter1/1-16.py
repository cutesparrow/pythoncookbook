#你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
newlist = [i for i in mylist if i > 0]
print(newlist)

new = (i for i in mylist if i > 0)
for i in new:
    print(i)
new = (i  if i > 0 else 0 for i in mylist)

for i in new:
    print(i)

def isInt(i):
    try:
        i = int(i)
        return True
    except:
        return False

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
result = list(filter(isInt,values))
print(result)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

boolList = [ n > 5 for n in counts]
result = list(compress(addresses,boolList))
print(result)
