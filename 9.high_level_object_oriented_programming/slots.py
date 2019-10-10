# 定义了一个class后，并创建了对应的实例后，可以给该实例绑定任何属性和方法
# __slots__可以限制实例的属性，但仅对当前类实例起作用！
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Jack'
s.age = 12
# s.score = 99 # 这个会报错
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 99
