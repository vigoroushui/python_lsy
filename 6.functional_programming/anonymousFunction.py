# lambda就是一个匿名函数
def build(x, y):
    return lambda: x * x + y * y

# 改写题
L = list(filter(lambda n : 1 == n % 2 , range(1, 20)))
print(L)