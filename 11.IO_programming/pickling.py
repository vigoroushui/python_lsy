# 序列化 程序运行时变量均存放在内存中
# 变量从内存中变成可存储或传输的过程称之为序列化
# 可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
# 把变量内容从序列化的对象重新读到内存里称之为反序列化
import pickle
d = dict(name = 'Bob', age = 20, score = 88)
pickle.dumps(d)

with open('a.txt', 'wb') as f:
    pickle.dump(d, f)
with open('a.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)

# JSON如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
# 更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取
# 也可以方便地存储到磁盘或者通过网络传输
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)

# 对于自定义类的处理, 只需要自定义转换函数即可
import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 88)
# print(json.dumps(s，default=student2dict)) 不够通用
print(json.dumps(s, default=lambda obj: obj.__dict__))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

#对中文的处理
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)