int('123456', base = 8)
int('1234', 16)
# 场景：如果需要大量的十进制数转化为二进制数，如此一个个写太过麻烦
def int2(x, base=2):
    return int(x, base)
# functools.partial就可以解决这个问题
import functools
int2 = functools.partial(int, base = 2)

max2 = functools.partial(max, 10)
max2(5, 6, 7) #相当于args = (10, 5, 6, 7)
              #      max(*args)
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。