from collections import deque
def lastSentence(fileContent,history):
    container = deque(maxlen=history)
    for i in fileContent:
        yield i,container
        container.append(i)

with open('./yield.txt','r') as f:
    for line,container in lastSentence(f,5):
        print('current line = ',line)
        print('current container = ',container)
        print('*'*20)


