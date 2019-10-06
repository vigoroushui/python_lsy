# 编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('start call')
        fn = func(*args, **kw)
        print('end call')
        return fn
    return wrapper

@log
def now():
    print('2019-10-06')

now()

# 编写一个能实现自定义文本或者不自定义文本的log
def log1(text)：
#还未完成