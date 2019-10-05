import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)) & isinstance(b, (int, float)) & isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    ans_1 = (-b + math.sqrt(b*b - 4*a*c)) / (2 * a)
    ans_2 = (-b - math.sqrt(b*b - 4*a*c)) / (2 * a)
    return ans_1, ans_2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')