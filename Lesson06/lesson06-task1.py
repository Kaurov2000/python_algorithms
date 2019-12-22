# Ubuntu 18.04 64 x86_64 Python 3.6

# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

import sys
from collections import deque
import timeit
import random


def show_size(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size = size + sys.getsizeof(key)
                size = size + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                size = size + sys.getsizeof(item)
    return size


# s = input("Введите натуральное число: ")
length = 80
l = [str(random.randint(0, 9)) for i in range(length)]
s = ''.join(l)
print("Строка, введенная пользователем, занимает {} байт".format(show_size(s)))


# Variant 1
memory = 0
res = ''
memory = memory + show_size(res)
for i in s:
    res = i + res
    memory = memory + show_size(res)
memory = memory + show_size(i)

print(res)
print("Первый вариант использует {} байт памяти".format(memory))


# Variant 2
memory = 0
num = int(s)
memory = memory + show_size(num)
res = 0
while num > 0:
    res = res * 10 + num % 10
    num = num // 10
memory = memory + show_size(res)
print(res)
print("Второй вариант использует {} байт памяти".format(memory))


# Variant 3
memory = 0
res = deque(s)
res.reverse()
memory = memory + show_size(res)
print(res)
print("Третий вариант использует {} байт памяти".format(memory))


var_1 = """
def var1(s):
    res = ''
    for i in s:
        res = i + res

var1(s)
"""

var_2 = """
def var2(s):
    num = int(s)
    res = 0
    while num > 0:
        res = res * 10 + num % 10
        num = num // 10
        
var2(s)
"""

var_3 = """
res = deque(s)
res.reverse()
"""

print(timeit.timeit(var_1, number = 1000,globals=globals()))
print(timeit.timeit(var_2, number = 1000,globals=globals()))
print(timeit.timeit(var_3, number = 1000,globals=globals()))

# length = 20, введенная строка занимает 69 байт
# length = 20, введенная строка занимает 89 байт
# length = 20, введенная строка занимает 129 байт


# length = 20 variant 1 : 0.0019488619873300195 секунд, 1289 байт
# length = 40 variant 1 : 0.0037556910247076303 секунд, 2879 байт
# length = 80 variant 1 : 0.007343006000155583 секунд, 7259 байт

# length = 20 variant 2 : 0.00680605397792533 секунд, 72 байт
# length = 40 variant 2 : 0.020645489013986662 секунд, 88 байт
# length = 40 variant 2 : 0.029751940979622304 секунд, 120 байт

# length = 20 variant 3 : 0.0005131429934408516 секунд, 1632 байт
# length = 40 variant 3 : 0.000730607018340379 секунд, 2632 байт
# length = 40 variant 3 : 0.0011848080030176789 секунд, 5160 байт

# Вывод:
# Метод "Variant 2" с переводом в тип int является самым эффективным по памяти, но не самым эффективным по процессору
# Метод "Variant 3" с deque не самый лучший по памяти, но зато самый эффективный по использованию процессора
# Метод "Variant 1" с переворотом строки - самый плохой из всех трех по совокупности характеристик
