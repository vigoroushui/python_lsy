from collections import Iterable
def findMinAndMax(L):
    if not isinstance(L,Iterable):
        raise TypeError ('input Type error')
    if [] == L:
        return (None, None)
    min = L[0]
    max = L[0]
    for i in L:
        if min > i:
            min = i
        if max < i:
            max = i
    return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 另一种简单的写法
def findMaxAndMin(L):
    if 0 == len(L):
        return (None, None)
    Min = Max = L[0]
    for i in L:
        Max = i if Max < i else Max
        Min = i if Min > i else Min
    return (Min, Max)

    # 测试
if findMaxAndMin([]) != (None, None):
    print('测试失败!')
elif findMaxAndMin([7]) != (7, 7):
    print('测试失败!')
elif findMaxAndMin([7, 1]) != (1, 7):
    print('测试失败!')
elif findMaxAndMin([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')