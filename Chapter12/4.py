from threading import Lock,Thread
import time
def incre(number,lock):
    while True:
        with lock:
            number[0]+=1
        time.sleep(1) 
        print(number[0])

def decr(number,lock):
    while True:
        time.sleep(1) 
        with lock:
            number[0]-=1
        print(number[0])
lock = Lock()
number = [10]
t1 = Thread(target=incre,args=(number,lock))
t2 = Thread(target=decr,args=(number,lock))
t1.start()
t2.start()
