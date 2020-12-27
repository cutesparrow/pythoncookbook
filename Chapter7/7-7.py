#如果你想让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可，就像下面这样：
x = 10
a = lambda y,x=x:x+y
x = 20
b = lambda y,x=x:x+y
a(10)
#20
b(20)
#30
funcs = [lambda x:x+n for n in range(5)]
for i in funcs:
    print(i(0))
func = [lambda x,n=n:x+n for n in range(5)]
for i in func:
    print(i(0))
