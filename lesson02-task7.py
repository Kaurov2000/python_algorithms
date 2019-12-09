# блок-схема https://drive.google.com/file/d/1dEhDcvqm2G2_TLmaHWJjhHq690VGGgVm/view?usp=sharing

def n_sum(x):
    if x == 1:
        return x
    else:
        return x + n_sum(x-1)

n = int(input("Введите натуральное число: "))
expr1 = n_sum(n)
expr2 = (n + 1) * n / 2
if expr1 == expr2:
    print("Гипотеза верна")
else:
    print("Гипотеза не верна")
