from time import time
from functools import wraps  #берет документацию из исходной функции


def decorator(param):
    def real_decorator(obj):
        @wraps(obj)
        def wrapper(*args):
            sumtime = 0
            for _ in range(param):
                t1 = time()
                res = obj(*args)
                t2 = time()
                delta = t2 - t1
                sumtime += delta
            return res, delta
        return wrapper
    return real_decorator

@decorator(100)

def func(a,b):
    """
    Исходная функция
    """
    return a ** b

print(func(2,3))
# print(decorator(100)(func)(2,3))
# print(func.__doc__)
print(func.__name__)