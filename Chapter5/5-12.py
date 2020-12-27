import os
path = 'somepath'
os.path.exists(path)
os.path.isdir(path)
os.path.isfile(path)
os.path.isline(path)
os.path.realpath(path)
os.path.getsize(path)
os.path.getmtime(path)
import time
time.ctime(os.path.getmtime(path))
