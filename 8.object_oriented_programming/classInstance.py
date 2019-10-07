# 一个简单的学生类，继承Object
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

#对象的实例化
Lisa = Student('Lisa', 97)
Jack = Student('Jack', 88)

print(Lisa.get_grade())
print(Jack.name)