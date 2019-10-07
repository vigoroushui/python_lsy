# 如何获取对象的类型和对象的方法？

# 1.使用type()，此函数返回值是对应的类型 （类型判断）
print(type(123) == int)
print(type('abc') == str)
print(type('abc') == type(123))
# 判断对象是否是函数
import types
def func():
    pass
type(func)==types.FunctionType
print(type(func), type(abs),type(lambda x: x),type(i for i in range(1,10)))

# 2.使用isinstance(), 对于class的继承关系 （类型判断）
#a = Animal()
#d = Dog()
#h = Husky()
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
#print(isinstance(h, Husky)) # True
#print(isinstance(h, Dog)) # True
isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))

# 3.使用dir(), 获得一个对象的所有属性和方法
dir('ABC')
len('ABC') # 等价于'ABC'.__len__()
class myDog(object):
    def __len__(self):
        return 100
dog = myDog()
print(len(dog))
# hasattr setattr getattr
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'), hasattr(obj, 'y'))
print(setattr(obj, 'y', 8), getattr(obj, 'y')) 
print(obj.y)
print(hasattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())

# 使用获取对象信息的函数时，注意不要画蛇添足（明明知道其中有某个方法，还写一个调用）
# 正确的使用方法，读取文件流fp中的图像
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None