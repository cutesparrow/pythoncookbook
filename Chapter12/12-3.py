#你的程序中有多个线程，你需要在这些线程之间安全地交换信息或数据
from queue import Queue
from threading import Thread
def preducer(out_q):
    while True:
        out_q.put(data)
def consumer(in_q):
    while True:
        data = in_q.get()

q = Queue()
t1 = Thread(target=preducer,args=(q,))
t2 = Thread(target=consumer,args=(q,))
t1.start()
t2.start()
#Queue 对象已经包含了必要的锁，所以你可以通过它在多个线程间多安全地共享数据。 当使用队列时，协调生产者和消费者的关闭问题可能会有一些麻烦。一个通用的解决方法是在队列中放置一个特殊的值，当消费者读到这个值的时候，终止执行。
import heapq
import threading
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()
    def put(self,item,priority):
        with self._cv:
            heapq.heappush(self.queue,(-priority,self._count,item))
            self._count+=1
            self._cv.notify()
    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]
def producer(out_q):
    while running:
        out_q.put(data)
def consumer(in_q):
    while True:
        data = in_q.get()
        in_q.task_done()
q = Queue()
t1 = Thread(target=consumer,args=(q,))
t2 = Thread(target=consumer,args=(q,))
t1.start()
t2.start()
#使用线程队列有一个要注意的问题是，向队列中添加数据项时并不会复制此数据项，线程间通信实际上是在线程间传递对象引用。如果你担心对象的共享状态，那你最好只传递不可修改的数据结构（如：整型、字符串或者元组）或者一个对象的深拷贝。
import copy
copy.deepcopy(data)
