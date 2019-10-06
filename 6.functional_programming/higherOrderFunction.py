#函数本身可以赋值给变量，即变量可以指向函数
f = abs
print(f(-10))

#函数名也是变量
#abs = 10
#print(abs)
print(abs(-10)) #此时abs()失效了

#高阶函数
def add(x, y, f):
    return f(x) + f(y)
print(add(10, -10, abs))

#map()的用法
print(list(map(str,[1, 2, 3, 4, 5, 6, 7])))
print(list(map(abs,[1, -1, -2, 3, 4, 5, -6])))

#reduce()的用法
#把str转换成int
from functools import reduce 
def strToInt(s):
    tmp = {'0':0, '1':1, '2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return tmp[s]
def func(x, y):
    return x * 10 + y
print(reduce(func, map(strToInt,'1234566')))

#抽象成一个函数
Digits = {'0':0, '1':1, '2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def funcc(x, y):
        return x * 10 + y
    def char2num(c):
        return Digits[c]
    return reduce(funcc, map(char2num, s))
print(str2int('21244'))

# 使用lambda表达式
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2Num(c):
    return DIGITS[c]
def str2Int(s):
    return reduce(lambda x, y : x * 10 + 10, map(char2Num,s))

#把一个字符串中的空字符删掉
def notEmpty(s):
    return s and s.strip()
print(list(filter(notEmpty,['1', '2', '', None, '21' , '2', '   '])))

#构造素数
def oddIter():
    n = 1
    while True:
        n += 2
        yield n
def notDivisible(n):
    return lambda x : x % n > 0

def prime():
    yield 2
    it = oddIter()
    while True:
        n = next(it)
        yield n
        it = filter(notDivisible(n), it)

for n in prime():
    if n < 1000:
        print(n)
    else:
        break

# sorted
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

