#你的程序要创建大量(可能上百万)的对象，导致占用很大的内存。
#对于主要是用来当成简单的数据结构的类而言，你可以通过给类添加 __slots__ 属性来极大的减少实例所占的内存。
class Date:
    __slots__ = ['year','month','day']
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
#当你定义 __slots__ 后，Python就会为实例使用一种更加紧凑的内部表示。 实例通过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典，这跟元组或列表很类似。 在 __slots__ 中列出的属性名在内部被映射到这个数组的指定小标上。 使用slots一个不好的地方就是我们不能再给实例添加新的属性了，只能使用在 __slots__ 中定义的那些属性名。


