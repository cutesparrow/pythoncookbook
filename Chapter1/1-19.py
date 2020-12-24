nums = [1,2,3,2,4]
result = sum(i * i for i in nums)
print(result)
import os
files = os.listdir('/Users/gaoyushi/Documents')
if any(name.endswith('.py') for name in files):
    print('there is python file')
else:
    print('there is no python file')

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
