#你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭代访问。
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]


from operator import itemgetter
rows.sort(key=itemgetter('date'))
from itertools import groupby
for date,items in groupby(rows,key = itemgetter('date')):
    print(date+":")
    for i in items:
       print(i)

#use defaultdict
from collections import defaultdict
d = defaultdict(list)
for row in rows:
    d[row['date']].append(row['address'])
print(d)
