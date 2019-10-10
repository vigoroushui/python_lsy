# 读写文件，法一
f = open('/home/xuyuhui/a.txt', 'r')
print(f.read())
f.close()

# 读写文件，法二
try:
    f = open('/home/xuyuhui/a.txt', 'r')
    print(type(f))
    print(f.read())
finally:
    if f:
        f.close()

#读写文件最好的方法
with open('/home/xuyuhui/a.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'去掉

# read() 一次读取全部内容
# readline() 一次读取一行内容
# readlines() 一次按行读取全部内容
# read(size) 指定读取大小

# 读取视频、图片等 要用二进制模式
with open('/home/xuyuhui/picture.jpg', 'rb') as f1:
    print(f1.read(10))

# 字符编码，指定读取GBK编码的文件
with open('/home/xuyuhui/a.txt', 'r', encoding = 'gbk', errors = 'ignore') as f2:
    print(f2.read())

# 写文件和读文件类似，只是mode为'w'，如果是在源文件基础上追加，则为'wa'
with open('/home/xuyuhui/a.txt', 'a+', encoding = 'gbk', errors = 'ignore') as f3:
    f3.write('I\'m the append part')
    print(f3.read())

