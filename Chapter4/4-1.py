def manulIter():
    with open('../Chapter1/yield.txt') as f:
        try:
            while True:
                line = next(f)
                print(line,end='')
        except StopIteration:
            pass

def manulIter2():
    with open('../Chapter1/yield.txt') as f:
        while True:
            line = next(f,None)
            if line:
                print(line,end='')
            else:
                break
if __name__ == '__main__':
    manulIter2()
