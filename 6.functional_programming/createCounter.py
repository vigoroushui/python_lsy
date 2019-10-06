# 方法一
def createCounter():
    a = 0
    def counter():
        nonlocal a
        a += 1
        return a
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# 方法二
def createCounter():
    s = [0]
    def counter():
        s[0] = s[0] + 1
        return s[0]
    return counter