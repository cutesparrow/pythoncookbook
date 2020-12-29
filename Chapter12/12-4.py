#你需要对多线程程序中的临界区加锁以避免竞争条件。
import threading
class SharedCounter:
    def __init__(self,initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()
    def incr(self,delta=1):
        with self._value_lock:
            self._value+=delta
    def decr(self,delta=1):
        with self._value_lock:
            self._value-=delta
#Lock 对象和 with 语句块一起使用可以保证互斥执行，就是每次只有一个线程可以执行 with 语句包含的代码块
#最好只在临界区（对临界资源进行操作的那部分代码）使用锁。
# 为了避免出现死锁的情况，使用锁机制的程序应该设定为每个线程一次只允许获取一个锁。

