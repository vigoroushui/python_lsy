def person(name, age, **kw):
    print('name', name, 'age:', age, 'other',kw)

print(person('Michael', 30))
print(person('Bob', 35, city='Beijing'))
print(person('Adam', 45, gender='M', job='Engineer'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city = extra['city'], job = extra['job']))
print(person('Jack', 24, **extra))

#命名关键字，可以有缺省值
def person_1(name, age, *, city='Beijing', job):
    print(name, age, city, job)

print(person_1('Jack', 24, job='Engineer'))

def person_2(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass