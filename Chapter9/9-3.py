#假设装饰器是通过 @wraps (参考9.2小节)来实现的，那么你可以通过访问 __wrapped__ 属性来访问原始函数：
'''
>>> @somedecorator
>>> def add(x, y):
...     return x + y
...
>>> orig_add = add.__wrapped__
>>> orig_add(3, 4)
7
'''
