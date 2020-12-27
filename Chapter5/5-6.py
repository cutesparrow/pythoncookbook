#使用 io.StringIO() 和 io.BytesIO() 类来创建类文件对象操作字符串数据
import io
s = io.StringIO()
s.write('Hello world\n')
print('this is a test ',file=s)
a = s.readlines()
print(s)
a = io.StringIO(s.getvalue())
print(a.read())
s = io.StringIO('hello world')
print(s.read(4))
print(s.read())
#io.StringIO 只能用于文本。如果你要操作二进制数据，要使用 io.BytesIO 类来代替。
