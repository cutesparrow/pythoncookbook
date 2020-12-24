#如果你的程序包含了大量无法直视的硬编码切片，并且你想清理一下代码。
record = '....................100 .......513.25 ..........'
SHARES = slice(20,23)
PRICE = slice(32,37)
cost = int(record[SHARES])*float(record[PRICE])
print(cost)
#内置的 slice() 函数创建了一个切片对象。所有使用切片的地方都可以使用切片对象。
sentence = 'this is a test sentence'
example = slice(3,10,2)
print(example.start)
print(example.stop)
print(example.step)
print(str(sentence[example]))
# si
#你还可以通过调用切片的 indices(size) 方法将它映射到一个已知大小的序列上
example = slice(3,100,2)
s = example.indices(len(sentence))
#这个方法返回一个三元组 (start, stop, step)
for i in range(*s):
    print(sentence[i])

print(s)
