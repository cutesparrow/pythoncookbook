a = [1, 2, 3, 4]
for i in reversed(a):
    print(i)
#反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。 如果两者都不符合，那你必须先将对象转换为一个列表才行
f = open('../Chapter1/yield.txt')
for i in reversed(list(f)):
    print(i)


class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
c = CountDown(10)
for i in c:
    print(i)
for i in reversed(c):
    print(i)
