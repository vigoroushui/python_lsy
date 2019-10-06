# 返回求和函数的函数
def lazySum(*args):
    def sum():
        ax = 0
        for i in args:
            ax += i
        return ax
    return sum

f = lazySum(1, 3, 5, 7, 9)
print(f())

# 闭包的例子
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3()) # 输出结果：9 9 9
# 非要使用循环变量的方法
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count1() 
print(f1(), f2(), f3()) # 输出结果：1 4 9


