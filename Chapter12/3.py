from queue import Queue
from threading import Thread
import time

def productor(out_q):
    n = 1
    while n<10:
        time.sleep(1)
        out_q.put(n)
        n+=1

def customer(in_q):
    while True:
        data = in_q.get()
        if data:
            print('using',data)

q = Queue()
t1 = Thread(target=productor,args=(q,))
t2 = Thread(target=customer,args=(q,))
t1.start()
t2.start()
