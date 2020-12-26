from itertools import permutations
items = ['a','b','c']
for i in permutations(items,2):
    print(i)
print('*'*20)
from itertools import combinations
for i in combinations(items,2):
    print(i)
print('*'*20)
from itertools import combinations_with_replacement
for i in combinations_with_replacement(items,2):
    print(i)
