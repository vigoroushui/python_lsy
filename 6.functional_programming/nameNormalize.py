#第一题
def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#第二题
from functools import reduce
def prod(L):
    return reduce(lambda x, y : x * y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#第三题, 注意括号匹配！！
from functools import reduce
def str2float(s):
    digital = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    n = s.find('.')
    def char2int(c):
        return digital[c]
    return reduce(lambda x, y: x * 10 + y, map(char2int,s[:n])) + reduce(lambda x, y: x * 10 + y, map(char2int,s[n+1:])) / (10**len(s[n+1:]))

print(str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')