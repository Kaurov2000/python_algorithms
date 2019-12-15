# Задание (№7 из 2го урока):
# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

import timeit
import cProfile
import sys

sys.setrecursionlimit(2000)

# Вариант 1 с рекурсией

def n_sum(x):
    if x == 1:
        return x
    else:
        return x + n_sum(x-1)

def variant_1(n):
    expr1 = n_sum(n)
    expr2 = (n + 1) * n / 2
    return expr1, expr2

var1 = """
def n_sum(x):
    if x == 1:
        return x
    else:
        return x + n_sum(x-1)

def variant_1(n):
    expr1 = n_sum(n)
    expr2 = (n + 1) * n / 2
    return expr1, expr2
    
variant_1(1000)
"""

# ################################################################
# Вариант 2 с циклом

def n_sum2(x):
    sum_ = x
    for i in range(x):
        sum_ = sum_ + i
    return sum_

def variant_2(n):
    expr1 = n_sum(n)
    expr2 = (n + 1) * n / 2
    return expr1, expr2

var2 = """
def n_sum2(x):
    sum_ = x
    for i in range(x):
        sum_ = sum_ + i
    return sum_

def variant_2(n):
    expr1 = n_sum2(n)
    expr2 = (n + 1) * n / 2
    return expr1, expr2
    
variant_2(1000)
"""

def main():
    n = int(input("Введите натуральное число: "))
    expr1, expr2 = variant_1(n)
    print("Вариант 1")
    if expr1 == expr2:
        print("Гипотеза верна")
    else:
        print("Гипотеза не верна")
    expr1, expr2 = variant_2(n)
    print("Вариант 2")
    if expr1 == expr2:
        print("Гипотеза верна")
    else:
        print("Гипотеза не верна")

if __name__ == '__main__':
    # main()
    # print(timeit.timeit(var1, number = 1000))
    print(timeit.timeit(var2, number = 1000))

# variant_1(25): 0.006002801994327456
# variant_1(50): 0.01236832799622789
# variant_1(100): 0.027906244969926775
# variant_1(200): 0.058381223992910236
# variant_1(500): 0.17491794604575261
# variant_1(1000): 0.5168532319949009
# Сложность O(N**2)

# variant_2(25): 0.002373583964072168
# variant_2(50): 0.004099957994185388
# variant_2(100): 0.007421275018714368
# variant_2(200): 0.014073172002099454
# variant_2(500): 0.037164031993597746
# variant_2(1000): 0.0827585730003193
# Сложность O(N)