from enum import Enum, unique
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique # 检查保证没有重复值
class Weekday(Enum):
    Sun = 0 
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
day1 = Weekday.Mon
day2 = Weekday['Tue']
day3 = Weekday.Tue.value
print(day1, day2, day3, Weekday(1), Weekday(Weekday.Mon))