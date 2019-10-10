# type既可以返回一个对象的类型，也可以创建出新的类型
class Hello(object):
    def hello(self, name = 'world'):
        print('hello, %s' % name)

def func(self, name = 'world'):
    print('hello, %s' % name)
Hello1 =type('Hello1', (object,), dict(hello = func) )
h = Hello1()
h.hello()

# metaclass mark后续有合适应用场景再仔细研究