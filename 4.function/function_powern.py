def powern(x, n=2):
    tmp = 1
    while n > 0:
        tmp = tmp * x
        n = n - 1 
    return tmp

print(powern(5, 50)) 