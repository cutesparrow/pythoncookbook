#你想给某个实例attribute增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证。
class Person:
    def __init__(self,first_name):
        self.first_name = first_name
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError('expected a string')
        self._first_name = value
    @first_name.deleter
    def first_name(self):
        raise AttributeError('can not delete attribute')
#上述代码中有三个相关联的方法，这三个方法的名字都必须一样。 第一个方法是一个 getter 函数，它使得 first_name 成为一个属性。 其他两个方法给 first_name 属性添加了 setter 和 deleter 函数。 需要强调的是只有在 first_name 属性被创建后， 后面的两个装饰器 @first_name.setter 和 @first_name.deleter 才能被定义。
a = Person('s')
print(a.first_name)
a.first_name = 'a' 
print(a.first_name)
#还能在已存在的get和set方法基础上定义property。例如：
class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)

b = Person2('name')
print(b.name)
