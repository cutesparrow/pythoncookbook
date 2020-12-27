#你有一个被其他python代码使用的callable对象，可能是一个回调函数或者是一个处理器， 但是它的参数太多了，导致调用时出错。
def spam(a,b,c,d):
    print(a,b,c,d)

from functools import partial
s1 = partial(spam,3)
s2 = partial(spam,d=42)
s2(1,2,3)
