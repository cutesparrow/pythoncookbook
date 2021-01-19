from threading import Thread, Event
import time
def countdown(n,start_event):
    print('count starting')
    start_event.set()
    while n>0:
        print('T-minus',n)
        n-=1
        time.sleep(1)

start_event = Event()

print('launching countdown')
t = Thread(target=countdown,args=(10,start_event))
t.start()

start_event.wait()
print('countdown is running')
t.join()
print('countdown finished')
