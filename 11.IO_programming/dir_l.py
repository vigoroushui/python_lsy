# coding=utf-8
# 利用os模块编写一个能实现dir -l输出的程序。
# 实现该命令的关键在于如何将二进制的字符转为权限码，如何遍历获得当前目录下文件个数，如何知道文件的状态
import os, time
dirpath = '.'
# 获取文件夹下文件个数，只取一层
def numOfFile(path, num=1):
    try:
        if os.path.isdir(path):
            for x in os.listdir(path):
                    num += 1
    except BaseException as e:
        pass
    finally: 
        return num

# 把二进制字符转换成权限码
# 读=4，写=2，可执行=1
def strtoWord(numstr):
    wordstr = ''
    words = ['r','w','x']
    # print(numstr) # 举例：111 000 000 (700)
    for i, x in enumerate(numstr): # i为字符串的下标, x为字符numstr[i]的值
        if x == '1':
            wordstr += (lambda i, words : words[i % 3])(i, words)
            # print(i, words[i % 3], wordstr)
        else:
            wordstr += '-'
    return wordstr

def listFile(path):
    print('权限\t        文件数\t用户Id\t群组Id\t大小\t月份\t日期\t时间\t文件名')
    for x in os.listdir(path):
        dir = os.path.join(path, x)
        stat = os.stat(dir)
        if os.path.isdir(dir):
            tmp = 'd'
        else:
            tmp = '-'
        print(tmp, strtoWord(str((bin(stat.st_mode)[-9:]))), end='\t') # 把权限码转为二进制，而后转为string，并只取后9位为权限码的二进制数
        print(numOfFile(dir), end='\t')
        print(stat.st_uid, end='\t')
        print(stat.st_gid, end='\t')
        print(stat.st_size, end='\t')
        mtime = time.localtime(stat.st_mtime)
        print(mtime.tm_mon, end='\t')
        print(mtime.tm_mday, end='\t')
        print(str(mtime.tm_hour)+':'+str(mtime.tm_min), end='\t')
        print(x)

listFile(dirpath)
'''
struct stat {
    dev_t         st_dev;       //文件的设备编号
    ino_t         st_ino;       //节点
    mode_t        st_mode;      //文件的类型和存取的权限
    nlink_t       st_nlink;     //连到该文件的硬连接数目，刚建立的文件值为1
    uid_t         st_uid;       //用户ID
    gid_t         st_gid;       //组ID
    dev_t         st_rdev;      //(设备类型)若此文件为设备文件，则为其设备编号
    off_t         st_size;      //文件字节数(文件大小)
    unsigned long st_blksize;   //块大小(文件系统的I/O 缓冲区大小)
    unsigned long st_blocks;    //块数
    time_t        st_atime;     //最后一次访问时间
    time_t        st_mtime;     //最后一次修改时间
    time_t        st_ctime;     //最后一次改变时间(指属性)
}
'''