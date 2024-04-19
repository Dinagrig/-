# 1

def f_1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n > 2:
        return f_1(n-1)*n + f_1(n-2)*(n-1)


def f_3(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return f_3(n-1) - f_3(n-2) + 2*n


def f_5(n):
    if n == 1:
        return 1
    elif n % 2 == 1 and n > 1:
        return n + f_5(n-2)
    elif n % 2 == 0:
        return n*f_5(n-1)


def f_7(n):
    if n < 3:
        return 1
    elif n > 2:
        x = 0
        for i in range(1, n):
            x += f_7(i)
        return x


f_9_list = [1000]


def f_9(n):
    if n >= 1000:
        return 1000
    elif n < 1000 and n % 2 == 1:
        None
    elif n < 1000 and n % 2 == 0:
        None

print(1, f_1(5))
print(3, f_3(6))
print(5, f_5(40))
print(7, f_7(18))
