#你已经启动了一个线程，但是你想知道它是不是真的已经开始运行了。
#下边的代码展示了如何使用 Event 来协调线程的启动：
from threading import Event,Thread
import time
def countdown(n,start_event):
    print('countdown start')
    start_event.set()
    while n>0:
        print('T-minus',n)
        n-=1
        time.sleep(1)
#start_event = Event()
#print('Launching countdown')
#t = Thread(target=countdown,args=(10,start_event))
#t.start()
#start_event.wait()
print('countdown is running')
#如果一个线程需要不停地重复使用 event 对象，你最好使用 Condition 对象来代替。下面的代码使用 Condition 对象实现了一个周期定时器，每当定时器超时的时候，其他线程都可以监测到：
import threading
class PeriodTimer:
    def __init__(self,interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()
    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()
    def run(self):
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag^=1
                self._cv.notify_all()
    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()
ptimer = PeriodTimer(1)
ptimer.start()
def countdown(nticks):
    while nticks>0:
        ptimer.wait_for_tick()
        print('T-minus',nticks)
        nticks-=1
def countup(last):
    n = 0
    while n<last:
        ptimer.wait_for_tick()
        print('Counting',n)
        n+=1
threading.Thread(target=countdown,args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()
