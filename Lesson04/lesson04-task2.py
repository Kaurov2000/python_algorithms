# Задача:
# Написать два алгоритма нахождения i-го по счёту простого числа.
# * Без использования Решета Эратосфена;
# * Использовать алгоритм решето Эратосфена.
# Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

import timeit

n = 10000
# первые 1229 чисел
test_x = 200

def with_sieve(x):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res[x - 1]

var1 = """
n = 10000
def with_sieve(x):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res[x - 1]

with_sieve(test_x)
"""

def without_sieve(x):
    counter = 1
    num = 2
    while counter < x:
        num = num + 1
        for j in range (2, num):
            if num % j == 0:
                break
        else:
            counter += 1
    return num

var2 = """
n = 10000
def without_sieve(x):
    counter = 1
    num = 2
    while counter < x:
        num = num + 1
        for j in range (2, num + 1):
            if j == num:
                counter += 1
            elif num % j == 0:
                break
    return num

without_sieve(test_x)
"""

def without_sieve_2(x):
    counter = 1
    num = 2
    while counter < x:
        num = num + 1
        for j in range (2, (num // 2) + 1):
            if num % j == 0:
                break
        else:
            counter += 1
    return num

var3 = """
n = 10000
def without_sieve_2(x):
    counter = 1
    num = 2
    while counter < x:
        num = num + 1
        for j in range (2, (num // 2) + 1):
            if num % j == 0:
                break
        else:
            counter += 1
    return num
    
without_sieve_2(test_x)
"""

def main():
    x = int(input("Введите порядковый номер простого числа (не больше 1229): "))
    print('Алгоритм "Решето Эратосфена" дает результат {}'.format(with_sieve(x)))
    print('Алгоритм с остатком от деления дает результат {}'.format(without_sieve(x)))
    print('Усовершенствованный алгоритм с остатком от деления дает результат {}'.format(without_sieve_2(x)))

if __name__ == '__main__':
    #main()
    print(timeit.timeit(var1, number=1000, globals=globals()))
    print(timeit.timeit(var2, number=1000, globals=globals()))
    print(timeit.timeit(var3, number=1000, globals=globals()))

# var1, test_x = 25: 3.49143092501486
# var1, test_x = 50: 3.1462675517116496
# var1, test_x = 100: 3.192414523368761
# var1, test_x = 200: 3.196124629542723

# var2, test_x = 25: 0.10132221049960677
# var2, test_x = 50: 0.407710707951515
# var2, test_x = 100: 1.8201503096620262
# var2, test_x = 200: 8.541422408386907

# var3, test_x = 25: 0.060174547568173864
# var3, test_x = 50: 0.2081544066251988
# var3, test_x = 100: 0.7863965553688272
# var3, test_x = 200: 3.3009715371406774
