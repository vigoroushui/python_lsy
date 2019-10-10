# 直接把属性暴露出去，没办法检查参数。
class Student0(object):
    def __init___(self,score):
        return self.score 
s = Student0()
s.score = 99 # 这里可以任意修改，但成绩是有一定范围的

# 为了限制成绩的范围 ，之前可以设置一个set_grade()的方法，
# 但在这里引入装饰器@property的手法，给函数动态加上功能
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value
# 对实例属性进行操作的时候，该属性不是直接暴露的，而是通过getter和setter方法实现的
Jack = Student()
# Jack.score = 101
Jack.score = 99

#还可定义只读属性
class Student1(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property   
    def age(self):  #这就是一个只读属性
        return 2019 - self._birth
