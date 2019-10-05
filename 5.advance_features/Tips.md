# 1.切片

C++中针对字符串提供了很多截取函数，如`substring`，其实目的就时对字符串切片

Python中的切片操作应用广泛，对tuple、字符串、list都可以进行切片。

# 2.迭代和列表生成器

任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环，学会判断是否可迭代的方法。

运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。

# 3.生成器

要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

注意区分普通函数和generator函数，普通函数调用直接返回结果：
```python
>>> r = abs(6)
>>> r
6
```
generator函数的“调用”实际返回一个generator对象：

```python
>>> g = fib(6)
>>> g
<generator object fib at 0x1022ef948>
```
# 4.迭代器

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于`next()`函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过`iter()`函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用`next()`函数实现的