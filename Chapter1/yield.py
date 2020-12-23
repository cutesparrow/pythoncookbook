def readFile(fpath):
    BUFFERSIZE = 64
    with open(fpath,'r') as f:
        while True:
            block = f.read(BUFFERSIZE)
            if block:
                yield block
            else:
                return

a = readFile('./yield.txt')
print(next(a))
# or print(a.__next__()) also work
