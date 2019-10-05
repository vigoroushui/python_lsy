print(list(range(1, 11)))

L = []
for i in range(1,11):
    L.append(i*i)
print(L)

#更简单的写法

print(list(x*x for x in range(1,11)))

print(list(x*x for x in range(1,11) if 0 == x % 2))

print(list(m + n for m in 'ABC' for n in 'DRF'))

# 列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

d = {'x':'A', 'y':'B', 'z':'C'}
for k,v in d.items():
    print(k, '=', v)

print([key+'='+value for key,value in d.items()])

L=['Hello', 'World', 'IBM', 'Apple']
print(list(s.lower() for s in L))

# exercise add 'if' sentence

L1 = {'Hello', 'World', 18, 'Apple', None}
print(list(s.lower() for s in L1 if isinstance(s, str)))
