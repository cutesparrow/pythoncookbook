#你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代码难以阅读， 于是你想通过名称来访问元素。
from collections import namedtuple
s = namedtuple('Subscriber',['address','joined'])
sub = s('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.address,sub.joined)
