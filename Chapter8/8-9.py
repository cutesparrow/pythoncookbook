class String:
    def __init__(self,name):
        self.name = name
    def __get__(self,instance,cls):
        if instance is None:
            return self
        else:
            print(instance.__dict__)
            return instance.__dict__[self.name]
    def __set__(self,instance,value):
        if not isinstance(value,str):
            raise TypeError('is not a string')
        instance.__dict__[self.name] = value
    def __delete__(self,instance):
        del instance.__dict__[self.name]

class Person:
    firstName = String('firstName')
    lastName = String('lastName')
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
p = Person('gaoyu','shi')
print(p.firstName)
