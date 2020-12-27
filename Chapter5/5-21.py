#你需要将一个Python对象序列化为一个字节流，以便将它保存到一个文件、存储到数据库或者通过网络传输它。
import pickle

data = 'someObj'
f = open('somefile')
pickle.dump(data,f)
string = pickle.dumps(data)
data = pickle.load(f)
data = pickle.loads(string)
'''
>>> import pickle
>>> f = open('somedata', 'wb')
>>> pickle.dump([1, 2, 3, 4], f)
>>> pickle.dump('hello', f)
>>> pickle.dump({'Apple', 'Pear', 'Banana'}, f)
>>> f.close()
>>> f = open('somedata', 'rb')
>>> pickle.load(f)
[1, 2, 3, 4]
>>> pickle.load(f)
'hello'
>>> pickle.load(f)
{'Apple', 'Pear', 'Banana'}
>>>
'''
#你还能序列化函数，类，还有接口，但是结果数据仅仅将它们的名称编码成对应的代码对象。
# focus on security 
