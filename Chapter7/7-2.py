#你希望函数的某些参数强制使用关键字参数传递
#将强制关键字参数放到某个*参数或者单个*后面就能达到这种效果
def recv(maxsize,*,block):
    pass

recv(10,block=True)
