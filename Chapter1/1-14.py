#你想排序类型相同的对象，但是他们不支持原生的比较操作。
class User:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'User({})'.format(self.name)

users = [User(1,'ziven'),User(3,'sparrow'),User(2,'Gaoyu')]
sortedUsers = sorted(users,key=lambda u:u.id)
print(sortedUsers)
from operator import attrgetter
sortedUsers2 = sorted(users,key=attrgetter('id'))
print(sortedUsers2)
