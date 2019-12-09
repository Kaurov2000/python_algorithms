# блок-схема https://drive.google.com/file/d/1dEhDcvqm2G2_TLmaHWJjhHq690VGGgVm/view?usp=sharing

while True:
    a, sign, b = input("Введите арифметическую операцию, разделяя числа и знак операции пробелами: ").split()
    if sign != '0' and sign != '+' and sign != '-' and sign != '*' and sign != '/':
        sign = input("Знак операции введен неверно, повторите ввод знака: ")
    if sign == '0':
        break
    elif sign == '+':
        print(f"Результат сложения {int(a) + int(b)}")
    elif sign == '-':
        print(f"Результат вычитания {int(a) - int(b)}")
    elif sign == '*':
        print(f"Результат умножения {int(a) * int(b)}")
    else:
        if int(b) != 0:
            print(f"Результат деления {int(a) / int(b)}")
        else:
            print("На 0 делить нельзя")
