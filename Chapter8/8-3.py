#为了让一个对象兼容 with 语句，你需要实现 __enter__() 和 __exit__() 方法。 例如，考虑如下的一个类，它能为我们创建一个网络连接：
from socket import socket,AF_INET,SOCK_STREAM
class LazyConnection:
    def __init__(self,address,family = AF_INET,type = SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None
    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family,self.type)
        self.sock.connect(self.address)
        return self.sock
    def __exit__(self):
        self.sock.close()
        self.sock = None
#在需要管理一些资源比如文件、网络连接和锁的编程环境中，使用上下文管理器是很普遍的。 这些资源的一个主要特征是它们必须被手动的关闭或释放来确保程序的正确运行。 例如，如果你请求了一个锁，那么你必须确保之后释放了它，否则就可能产生死锁。 通过实现 __enter__() 和 __exit__() 方法并使用 with 语句可以很容易的避免这些问题， 因为 __exit__() 方法可以让你无需担心这些了。
#在第二个版本中，LazyConnection 类可以被看做是某个连接工厂。在内部，一个列表被用来构造一个栈。 每次 __enter__() 方法执行的时候，它复制创建一个新的连接并将其加入到栈里面。 __exit__() 方法简单的从栈中弹出最后一个连接并关闭它。 这里稍微有点难理解，不过它能允许嵌套使用 with 语句创建多个连接，就如上面演示的那样。
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()

# Example use
from functools import partial

conn = LazyConnection(('www.python.org', 80))
with conn as s1:
    pass
    with conn as s2:
        pass
