# 把下面的Student对象的gender字段对外隐藏起来，
# 用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def getGender(self):
        return self.__gender
    def setGender(self, gender):
        if(gender == 'male' or gender == 'female'):
            self.__gender = gender
        else:
            raise ValueError('bad gender')

bart = Student('Bart', 'male')
if bart.getGender() != 'male':
    print('测试失败!')
else:
    bart.setGender('female')
    if bart.getGender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')