#一个子类可以获得多个父类的所有功能
class Dog(Mammal, Runnable):
    pass
class Bat(Mammal, Flyable):
    pass

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass

# 多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
# 多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
# 多携程模式的TCP服务
class MyTCPServer(TCPServer, CoroutineMixIn):
    pass
