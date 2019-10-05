def product(ans,*args): # 需要添加一个可选参数ans
    # ans = 1 加上这句话会测试失败，因为product()不需要默认值
    for n in args:
        if not isinstance(n, (int, float)):
            continue
        ans = ans * n
    return ans

A = (1, 2, 3, 'a', 5.7)
print(A, product(*A))
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')