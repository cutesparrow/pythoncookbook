#你需要在程序执行时创建一个临时文件或目录，并希望使用完之后可以自动销毁掉。
from tempfile import TemporaryFile
with TemporaryFile('w+t') as f:
    f.write('something')
import tempfile
print(tempfile.gettempdir())
