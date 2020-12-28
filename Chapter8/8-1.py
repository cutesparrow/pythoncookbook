#要改变一个实例的字符串表示，可重新定义它的 __str__() 和 __repr__() 方法。
class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({},{})'.format(self.x,self.y)
    def __str__(self):
        return 'Pair({},{})'.format(self.x,self.y)


