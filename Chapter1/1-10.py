#怎样在一个序列上面保持元素顺序的同时消除重复的值？
def dedupe(items):
    seen = set()
    for i in items:
        if i not in seen:
            yield i
            seen.add(i)

def dedupe2(items,key=None):
    seen = set()
    for item in items:
        value = item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)


a = [1,2,3,4,3,3,2,2,1]
print(list(dedupe(a)))

b = [{'a':1},{'a':1}]
print(list(dedupe2(b,key=lambda s:s['a'])))
