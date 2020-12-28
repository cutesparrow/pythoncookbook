#你想封装类的实例上面的“私有”数据，但是Python语言并没有访问控制。
#Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果。 第一个约定是任何以单下划线_开头的名字都应该是内部实现。
class A:
    def __init__(self):
        self._internal = 0
        self.public = 1
    def public_method(self):
        pass
        # A public method
    def _internal_method(self):
        pass
        # A internal method which is private
    
#你还可能会遇到在类定义中使用两个下划线(__)开头的命名
#使用双下划线开始会导致访问名称变成其他形式。 比如，在前面的类B中，私有属性会被分别重命名为 _B__private 和 _B__private_method 。 这时候你可能会问这样重命名的目的是什么，答案就是继承——这种属性通过继承是无法被覆盖的
class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        pass
    def public_method(self):
        pass
        self.__private_method()
class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1
    def __private_method(self):
        pass
#这里，私有名称 __private 和 __private_method 被重命名为 _C__private 和 _C__private_method ，这个跟父类B中的名称是完全不同的。
#上面提到有两种不同的编码约定(单下划线和双下划线)来命名私有属性，那么问题就来了：到底哪种方式好呢？ 大多数而言，你应该让你的非公共名称以单下划线开头。但是，如果你清楚你的代码会涉及到子类， 并且有些内部属性应该在子类中隐藏起来，那么才考虑使用双下划线方案。
