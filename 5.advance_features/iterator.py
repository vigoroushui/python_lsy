# 区分iterable和iterator

from collections import Iterable, Iterator
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance(100,Iterator))


#  for 循环的本质
for x in [1, 2, 3, 4, 5]:
    pass

it = iter([1, 2, 3, 4]) # 首先得到一个iterator对象
while True:
    try:
        x = next(it)
    except StopIteration:
        break


