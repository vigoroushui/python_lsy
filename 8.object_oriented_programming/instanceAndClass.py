#区别，第一个是实例属性、第二个是类属性
def Student(object):
    def __init__(self, name):
        self.name = name

class Student1(object):
    name = 'Student'

# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字
# 因为相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

stu = Student1()
print(stu.name)
print(Student1.name)
stu.name = 'Jack'
print(stu.name)
print(Student1.name)
del stu.name
print(stu.name)