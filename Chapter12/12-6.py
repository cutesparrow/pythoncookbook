#你需要保存正在运行线程的状态，这个状态对于其他的线程是不可见的。
#它之所以行得通的原因是每个线程会创建一个自己专属的套接字连接（存储为self.local.sock）。 因此，当不同的线程执行套接字操作时，由于操作的是不同的套接字，因此它们不会相互影响。


from socket import socket, AF_INET, SOCK_STREAM
import threading

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected')
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.local.sock.close()
        del self.local.sock
#其原理是，每个 threading.local() 实例为每个线程维护着一个单独的实例字典。 所有普通实例操作比如获取、修改和删除值仅仅操作这个字典。 每个线程使用一个独立的字典就可以保证数据的隔离了。

