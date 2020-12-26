xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99,100]
for i,j in zip(xpts,ypts):
    print('i = {},j = {}'.format(i,j))
print('*'*20)
from itertools import zip_longest
for i,j in zip_longest(xpts,ypts,fillvalue=None):
    print('i = {},j = {}'.format(i,j))
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
print(dict(zip(headers,values)))
