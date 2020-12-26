from collections import deque

class linehistory:
    def __init__(self,lines,length):
        self.lines = lines
        self.history = deque(maxlen=length)
    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.history.append((lineno,line))
            yield line
    def clear(self):
        self.history.clear()

with open('/Users/gaoyushi/1.txt') as f:
    lines = linehistory(f,3)
    for line in lines:
        if 'python' in line:
            for lineno,line in lines.history:
                print('{}:{}'.format(lineno,line))

