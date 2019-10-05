def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

 # print(calc(1,2,3))
print(calc([1,2,3]))

def calc_1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc_1(1,2,3))

nums = [1, 2, 3]
print(calc([nums[0], nums[1], nums[2]]))
print(calc_1(*nums))
