d = {'a':1, 'b':2, 'c':3}
# key and value
for key,value in d.items():
    print(key, ':', value)

# 如何判断一个对象是否是可迭代对象？
from collections import Iterable
print(isinstance([1,2,3], Iterable))
print(isinstance('avcadwa',Iterable))
print(isinstance(1213,Iterable))

for i,value in enumerate(['a', 'b', 'c']):
    print(i,value)

for x, y in [(2,1), (2,2), (3,3)]:
    print(x)
