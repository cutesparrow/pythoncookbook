#你想定义一个可以接受参数的装饰器
from functools import wraps
import logging

def logged(level,name=None,message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logmsg)
            return func(*args,**kwargs)
        return wrapper
    return decorate
#定义一个接受参数的包装器看上去比较复杂主要是因为底层的调用序列。特别的，如果你有下面这个代码：

@decorator(x, y, z)
def func(a, b):
    pass
装饰器处理过程跟下面的调用是等效的;

def func(a, b):
    pass
func = decorator(x, y, z)(func)

