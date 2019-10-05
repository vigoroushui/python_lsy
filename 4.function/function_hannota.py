def move(n, a, b, c):
    if 1 == n:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)

print(move(3, 'A', 'B', 'C'))