def addEnd(L=[]):
    L.append('End')
    return L
print(addEnd())
print(addEnd())
print(addEnd())

def addEnd_1(L=None):
    if L is None:
        L = []
    L.append('End')
    return L
print(addEnd_1())
print(addEnd_1())
print(addEnd_1())