def mn1(n, m):
    if n > m:
        return 0
    elif n == m:
        return 1
    else:
        return mn1(n+1, m) + mn1(n+3, m) + mn1(n*2, m)


def mn2(n, m):
    if n > m or n == 17:
        return 0
    elif n == m:
        return 1
    else:
        return mn2(n+1, m) + mn2(n+2, m) + mn2(n*3, m)


def mn3(n, m):
    if n > m:
        return 0
    elif n == m:
        return 1
    else:
        return mn3(n+4, m) + mn3(n+2, m)


# def mn4(n, m):
#     if 1 == 1:
#         return 0
#     elif n == m:
#         return 1
#     else:
#         return mn4(n - 1, m) + mn4(n + 3, m) + mn4(n * 2, m)


def mn5(n, m):
    if n > m:
        return 0
    elif n == m:
        return 1
    else:
        return mn5(n+1, m) + mn5(n*4, m)


def mn6(n, m):
    if n > m:
        return 0
    elif n == m:
        return 1
    else:
        return mn6(n + 1, m) + mn6(n * 2, m)


def mn7(n, m):
    if n > m:
        return 0
    elif n == m:
        return 1
    else:
        return mn7(n + 1, m) + mn7(n + 2, m) + mn7(n*3, m)


def mn8(n, m):
    if n > m or n == 6 or n == 12:
        return 0
    elif n == m:
        return 1
    else:
        return mn8(n + 1, m) + mn8(n*2, m) + mn8(n + 3, m)


def mn9(n, m):
    if n > m:
        return 0
    elif n == m:
        return 1
    else:
        return mn9(n+1, m) + mn9(n*2, m) + mn9(n*3, m)


def mn10(n, m):
    if n > m or n == 59:
        return 0
    elif n == m:
        return 1
    else:
        return mn10(n + 1, m) + mn10(n * 2, m)


print(1, mn1(3, 12) * mn1(12, 16))
print(2, mn2(3, 10) * mn2(10, 25))
print(3, mn3(4, 22))
print(5, mn5(1, 29))
print(6, mn6(2, 11) * mn6(11, 25) * mn6(25, 50))
print(7, mn7(1, 10) * mn7(10, 15))
print(8, mn8(3, 16))
print(9, mn9(1, 13))
print(10, mn10(3, 14) * mn10(14, 62))
