#'解压可迭代对象赋值给多个变量'
a = [('foo',1,2),('doo',3,4)]
def foo(args):
    result = 0
    for i in args:
        result += i
    return result
def doo(args):
    result = 1
    for i in args:
        result *= i
    return result

for (function,*args) in a:
    if function == 'foo':
        print(foo(args))
    elif function == 'doo':
        print(doo(args))
