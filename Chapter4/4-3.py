#如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。
def frange(start, stop, increament):
    i = start
    while (i < stop):
        yield i
        i += increament
if __name__ == '__main__':
    print(list(frange(0,3,0.5)))

#一个生成器函数主要特征是它只会回应在迭代中使用到的 next 操作。 一旦生成器函数返回退出，迭代终止。我们在迭代中通常使用的for语句会自动处理这些细节，所以你无需担心。
