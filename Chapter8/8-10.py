#你想将一个只读属性定义成一个property，并且只在访问的时候才会计算结果。 但是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算。
class lazyProperty:
    def __init__(self,func):
        self.func = func
    def __get__(self,instance,cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance,self.func.__name__,value)
            return value
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    @lazyProperty
    def area(self):
        print('computing area')
        return math.pi * self.radius ** 2

