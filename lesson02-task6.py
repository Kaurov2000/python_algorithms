# блок-схема https://drive.google.com/file/d/1dEhDcvqm2G2_TLmaHWJjhHq690VGGgVm/view?usp=sharing

import random

x = random.randrange(0,101)
attempt = 0
print("Я загадал натуральное число от 0 до 100, попробуй его угадать")
while attempt < 10:
    attempt += 1
    y = int(input("Введите число: "))
    if x == y:
        break
    elif x > y:
        print("введенное число меньше")
    else:
        print("введенное число больше")
if attempt < 10:
    print("Угадал!")
else:
    print(f"Было загадано число {x}")