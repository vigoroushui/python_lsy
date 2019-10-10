class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Jack')) # <__main__.Student object at 0x7f2c1aa22c50>

# __str__特殊变量，可以让输出更加接近用户
class Student1(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student Object (name: %s)' % self.name
print(Student1('Jack')) # Student Object (name: Jack)
s = Student1('Jack')
s #在命令行模式下会出现<__main__.Student1 object at 0x7f2c1aa22c60> 此显示依旧不美观

class Student2(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student Object (name: %s)' % self.name
    __repr__ = __str__ #这是返回给程序开发者看的字符串，用于调试

#自定义一个斐波那契数列
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a

#for n in Fib():
#    print(n)

# __getitem__ 使类能够按下标取元素
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
print(Fib()[5])

# 修改类Fib()使其能够满足切片的要求, 没有对负数进行处理
class FibUp(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            if step is None:
                step = 1
            a, b = 1, 1
            L = []
            y = start
            for x in range(start, stop):
                if x >= start and x == y:
                    L.append(a)
                    y = x + step
                a, b = b, a + b
            return L
f = FibUp()
print(f[:10:2])

# __getattr__ 避免调用不存在的类方法或属性时报错的情况，该方法会动态的返回一个属性
class Student3(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if 'score' == attr:
            return 99
        if 'age' == attr:
            return lambda : 25
        raise AttributeError('\'Student3\'object has no attribute \'%s\'' % attr)
s = Student3()
print(s.name, s.score, s.age())

#可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段
#URL即网址的拼接
class Chain(object):
    def __init__(self, path = ''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status.user.timeline.list)
#print(Chain().users('michael').repos) # 'Chain' object is not callable

# 使上一个Chain类的实例化对象成为可调用(callable)即可
class Chain(object):
    def __init__(self, path = ''):
        self.__path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))
    def __call__(self, parameter):
        return Chain('%s/%s' % (self.__path, parameter))
    def __str__(self):
        return self.__path
    __repr__ = __str__

print(Chain().users('michael').repos)