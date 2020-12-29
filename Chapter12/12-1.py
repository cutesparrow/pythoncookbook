#你要为需要并发执行的代码创建/销毁线程
import time
def countdown(n):
    while n>0 :
        print('T-minus',n)
        n-=1
        time.sleep(5)

from threading import Thread
#t = Thread(target=countdown,args=(10,))
#t.start()
#t.join()
#print('go')
##你可以查询一个线程对象的状态，看它是否还在执行：
#if t.is_alive():
#    print('running')
#else:
#    print('completed')
#T-minus 10
#T-minus 9
#T-minus 8
#T-minus 7
#T-minus 6
#T-minus 5
#T-minus 4
#T-minus 3
#T-minus 2
#T-minus 1
#go
#completed
class CountdownTask:
    def __init__(self):
        self._running = True
    def terminate(self):
        self._running = False
    def run(self,n):
        while self._running and n>0:
            print('T-minus',n)
            n-=1
            time.sleep(1)
#c = CountdownTask()
#t = Thread(target=c.run,args=(10,))
#t.start()
#c.terminate()
#t.join()
class IOtask:
    def terminate(self):
        self._running = False
    def run(self,sock):
        sock.settimeout(5)
        while self._running:
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
        return

