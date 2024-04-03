

def fact(x):
    if x <= 1:
        return 1
    else:
        return x*fact(x-1)


def fib(n):
    if n < 2:
        return n
    elif n >= 2:
        return fib(n - 1) + fib(n-2)


def matryoshka(z):
    if z == 0:
        print('маленькая матрешечка 0')
    elif z > 0:
        print(f'верх матрешки {z}')
        matryoshka(z-1)
        print(f'низ матрешки {z}')


def gdc(a, b):
    if a == b:
        return a
    elif a > b:
        return gdc(a-b, b)
    elif a < b:
        return gdc(a, b-a)


# print(gdc(, ))

matryoshka(4)

# print(fib(3))
