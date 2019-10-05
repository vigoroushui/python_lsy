def fact(n):
    if 1==n:
        return 1
    return n * fact(n-1)

print(fact(5))


## 尾递归的方法，Python解释器并没有对其进行优化
def factIter(n):
    return factTail(n, 1)

def factTail(num, product):
    if 1==num:
        return product
    return factTail(num-1, product*num)

print(factIter(5))