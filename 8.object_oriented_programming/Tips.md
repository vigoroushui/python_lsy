# 继承与多态
- 多态真正的威力：调用方只管调用，不管细节，当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
- 以上也是著名的**开闭原则**：
    - 对扩展开放：允许新增Animal子类；
    - 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

Python是动态语言 ，`InheritanceAndPolymorphism.py`中的例子，它不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了。

> 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像 鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个`read()`方法，返回其内容。但是，许多对象，只要有`read()`方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了`read()`方法的对象。

实例属性属于各个实例所有，互不干扰；类属性属于类所有，所有实例共享一个属性；

**不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。**