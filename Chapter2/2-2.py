#你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme等等。
fileName = 'test.py'
print(fileName.endswith('.py'))
print(fileName.startswith('test'))
import os
fileNames = os.listdir('.')
result = [(name,True if name.endswith('.py') else False) for name in fileNames]
print(result)
print(any(name.endswith('.py') for name in fileNames))
choice = ['https://','http://']
from urllib.request import urlopen
def readUrl(address):
    if address.startswith(tuple(choice)):
        return urlopen(address).read()
    else:
        with open(address) as f:
            return f.read() 
print(readUrl('http://www.baidu.com'))
