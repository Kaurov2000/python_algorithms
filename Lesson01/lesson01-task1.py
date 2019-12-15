# Ссылка на схемы
# https://drive.google.com/file/d/14vLKzw007Cj8Ld8VYsGee5cxRGMk5lHL/view?usp=sharing

n = int(input("введите положительное целое трехзначное число: "))
c = n % 10
n = n // 10
b = n % 10
a = n // 10

sum = a + b + c
mul = a * b * c

print(f"Сумма цифр равна {sum}, произведение цифр равно {mul}")