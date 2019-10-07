# class定义的本身是一种数据类型，和Python内置的str list tuple没什么区别
class Animal(object):
    def run(self):
        print('Animal is running ...')

# 子类的方法可以覆盖父类的方法，这就是所谓的多态
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    pass

dog = Dog()
dog.run()

#测试dog究竟是什么类型
print(isinstance(dog, Dog), isinstance(dog, Animal)) # 双类型的dog!

# 理解多态
# 当我们需要传入Dog、Cat、……时，我们只需要接收Animal类型就可以了, 因为派生的类的都是Animal类型的，随后按照此类型操作即可
def runTwice(animal):
    animal.run()
    animal.run()
runTwice(Dog())
runTwice(Animal())

# 多态真正的威力：调用方只管调用，不管细节，
# 当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
# 以上也是著名的开闭原则：
#    对扩展开放：允许新增Animal子类；
#    对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。