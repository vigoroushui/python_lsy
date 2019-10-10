# 查看操作系统类型
import os
print(os.name)
print(os.uname)
print(os.environ)
print（os.environ.get('PATH')
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
# 路径拼接的方法
print(os.path.join('/home/xuyuhui', 'testdir')
# 创建一个目录
os.mkdir('/home/xuyuhui/testdir')
# 删掉一个目录
os.rmdir('/home/xuyuhui/testdir')

# 路径的拆分
print(type(os.path.split('/home/xuyuhui/a.txt'))) # <class 'tuple'> ('/home/xuyuhui', 'a.txt')
# 拆分后直接获得文件扩展名
print(type(os.path.splitext('/home/xuyuhui/a.txt'))) 

# 对文件重命名
os.rename('test.txt', 'test.py')
# 删掉文件
os.remove('test.py')

# 注意os模块中没有复制文件的函数

import shutil 
# shutil.copyfile()如此便可实现文件的复制

# 列出当前目录下所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])




