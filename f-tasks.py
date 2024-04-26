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


def f_9(n):
    if n >= 1000:
        return 1000
    elif n < 1000 and n % 2 == 1:
        return n * f_9(n+1)
    elif n < 1000 and n % 2 == 0:
        return n * (f_9(n+1)/2)


F10_list = [0]


def f_10(n):
    for i in range(len(F10_list), n + 1):
        F10_list.append(f_10(i//10))
    if n == 0:
        return F10_list[n]
    elif n > 0 and n % 2 == 0:
        return F10_list[n] + n % 10
    elif n % 2 == 1:
        return F10_list[n]


for i in range(10**9, 2 * 10**9 + 1):



f8_list = [10] * 11

def f_8(n):
    if n >= len(f8_list):
        for i in range(len(f8_list), n + 1):
            f8_list.append(f_8(i - 1))
        return n + f8_list[n]
    else:
        return f8_list[n]

def f_6(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f_6(n / 2)
    elif n % 2 == 1:
        return 1 + f_6(n - 1)

def f_4(n):
    if n < 3:
        return 2
    else:
        return 2 * f_4(n-1) + f_4(n-2)


def f_2(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    elif n > 3:
        return f_2(n - 3) + f_2(n - 2) + f_2(n-1)


print(1, f_1(5))
print(2, f_2(9))
print(3, f_3(6))
print(4, f_4(5))
print(5, f_5(40))
counter = 0
for n in range(1, 501):
    if f_6(n) == 3:
        counter += 1
print(6, counter)
print(7, f_7(18))
print(8, f_8(2021) - f_8(2019))
print(9, f_9(998)/f_9(1001))
# counter = 0
# for k in range(10**9, 2 * 10**9 + 1):
#     if f_10(k) == 0:
#         counter += 1
# print(counter)
