# 定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log  #相当于执行了now = log(now)
def now():
    print('2019-10-06')
now()

# 三层嵌套的日志，比如自定义log的文本
def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log1('test') #now = log('execute')(now)
def now1():
    print('2019-10-06')
now1()

# 函数也是对象，它有__name__等属性，
# 经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
# 所以此时需要将now.__name__赋值给wrapper.__name__
import functools

def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s' % func.__name__)
        return func(*args, **kw)
    return wrapper

import functools

def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator