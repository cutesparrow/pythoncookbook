#使用函数参数注解是一个很好的办法，它能提示程序员应该怎样正确使用这个函数。 例如，下面有一个被注解了的函数：
def add(x: int, y: int) -> int:
    return x + y
print(add.__annotations__)
