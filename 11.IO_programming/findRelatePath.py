import os
def findRelatePathIncludeString(str, dir = os.path.abspath('.')):
    for x in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, x)):
            findRelatePathIncludeString(str, os.path.join(dir, x))
        elif str in x:
            ans = os.path.split(os.path.join(dir, x))
            print(ans[1]) # 打印相对路径

print(findRelatePathIncludeString('find'))
        
