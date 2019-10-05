L = [x*x for x in range(10)]
L1 = (x*x for x in range(10))
print(next(L1))
print(next(L1))

for i in L1:
    print(i)
#期望输出十个数但是实际情况仅仅输出8个

#斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6))

# 将斐波那契数列改为生成器的形式 
def fib_1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b 
        n = n + 1
    return 'done'

f = fib_1(6)
print(f)

# 无法捕获函数的返回值
for n in fib_1(6):
    print(n)

# 捕获函数的返回值
g = fib_1(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
