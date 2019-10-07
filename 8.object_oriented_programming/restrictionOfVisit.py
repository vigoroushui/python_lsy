#私有、公有、保护属性，不同于C++。
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def getGrade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    def getName(self):
        return self.__name

Jack = Student('Jack',99)
Jack.__name = 'Bob' # 执行成功，但是会生成一个新的__name属性
                    # 真正的__name属性变成了_Student__name(因解释器不同而不同)
print(Jack.getName(), Jack.__name) # 验证代码

