from fnmatch import fnmatch,fnmatchcase
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
result = [name for name in names if fnmatch(name,'Dat*.csv')]
print(result)
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
result = [address for address in addresses if fnmatch(address,'*ST')]
print(result)
text1 = '11/27/2012'
import re
dateSearch = re.compile(r'(\d+)/(\d+)/(\d+)$')
result = dateSearch.match(text1)
print(result)
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.group(3))
print(result.groups())
for i in dateSearch.finditer(text):
    print(i.groups())
m = dateSearch.match('11/27/2012abcdef')
print(m)
