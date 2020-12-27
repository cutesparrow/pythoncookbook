#call back function
def apply_async(func,args,*,callback):
    result = func(*args)

    callback(result)
def print_result(result):
    print("Got:",result)

def add(x,y):
    return x+y
apply_async(add,(2,3),callback=print_result)
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence+=1
        print('[{}] Got:{}'.format(sequence,result))
    return handler
handler = make_handler()
apply_async(add,(2,3),callback=handler)
apply_async(add,(2,3),callback=handler)
def make_handler2():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
