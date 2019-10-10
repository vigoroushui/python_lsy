# 数据读写不一定是文件，可以在内存中读写
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# 可以用一个str初始化StringIO, 然后像读文件一样读取
f1 = StringIO('hello!\nHi!\nGoodbye!')
while True:
    s = f1.readline()
    if '' == s:
        break
    print(s.strip())

# BytesIO可以用来操作二进制数据
from io import BytesIO
f2 = BytesIO()
f2.write('中文'.encode('utf-8'))
print(f2.getvalue())

f3 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f3.read())
