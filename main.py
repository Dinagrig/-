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
    if b == 0:
        return a
    return gdc(b, a % b)


def pow1(a, n):
    print('лопух', a, n)
    if n == 0:
        return 1
    return a*pow1(a, n-1)


def pow2(a, n):
    print('щавель', a, n)
    if n == 0:
        return 1
    elif n % 2 != 0:
        return a * pow2(a, n - 1)
    elif n % 2 == 0:
        return pow2(a*a, n // 2)


fib_list = [0, 1]


def fib_dynamic(n):
    if n >= len(fib_list):
        for i in range(len(fib_list), n + 1):
            fib_list.append(fib_dynamic(i - 1) + fib_dynamic(i - 2))
    return fib_list[n]


for i in range(51):
    print(i, fib_dynamic(i))


# print(pow1(4, 10))

# print(pow2(4, 10))

# print(gdc(42, 48))

# print(gdc(, ))

# matryoshka(4)

# print(fib(3))
