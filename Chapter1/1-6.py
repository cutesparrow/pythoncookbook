from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['a'].append(3)
print(d)
