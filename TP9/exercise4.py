
import functools

def dec2int(alist):
    return functools.reduce(lambda x, y: x * 10 + y, alist)
