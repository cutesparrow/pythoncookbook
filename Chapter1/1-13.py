#你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
rowsByFname = sorted(rows,key=itemgetter('fname'))
print(rowsByFname)
rowsByUid = sorted(rows,key=lambda s:s['uid'])
print(rowsByUid)
rowsByUid2 = sorted(rows,key=itemgetter('uid'))
print(rowsByUid2)
rowsByFLname = sorted(rows,key=itemgetter('fname','lname'))
print(rowsByFLname)
