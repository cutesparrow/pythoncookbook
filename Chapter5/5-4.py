'''
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))
'''
import array
a = array.array('i',[1,2,3])
with open('testFor5-4.bin','wb') as f:
    f.write(a)
a = array.array('i',[0,0,0,0,0,0,0,0])
with open('testFor5-4.bin','rb') as f:
    f.readinto(a)
print(a)
