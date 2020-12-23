#怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

commonKeys = a.keys() & b.keys()
print(commonKeys)

commonItems = a.items() & b.items()
print(commonItems)

#in a but not in b
uniqueItems = a.items() - b.items()
print(uniqueItems)

c = {key:a[key] for key in a.keys() - ['z','w']}
print(c)
