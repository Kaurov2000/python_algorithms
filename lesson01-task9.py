# Ссылка на схемы
# https://drive.google.com/file/d/14vLKzw007Cj8Ld8VYsGee5cxRGMk5lHL/view?usp=sharing

a, b, c = map(float, input("введите три разных числа через пробел: ").split())

if a > b:
    if b > c:
        print(f"Среднее число {b}")
    elif a > c:
        print(f"Среднее число {c}")
    else:
        print(f"Среднее число {a}")
elif a > c:
    print(f"Среднее число {a}")
elif b > c:
    print(f"Среднее число {c}")
else:
    print(f"Среднее число {b}")
