#你想在函数上添加一个包装器，增加额外的操作处理(比如日志、计时等)。
import time
from functools import wraps


def timeThis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timeThis
def countDown(n):
    while n > 0:
        n -= 1

countDown(100)
#需要强调的是装饰器并不会修改原始函数的参数签名以及返回值。 使用 *args 和 **kwargs 目的就是确保任何参数都能适用。 而返回结果值基本都是调用原始函数 func(*args, **kwargs) 的返回结果，其中func就是原始函数。

