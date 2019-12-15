# блок-схема https://drive.google.com/file/d/1dEhDcvqm2G2_TLmaHWJjhHq690VGGgVm/view?usp=sharing

max_sum = 0
num_max_sum = 0
while True:
    x = input("Введите натуральное число или 0 для выхода: ")
    if x == '0':
        break
    else:
        cur_sum = 0
        for i in x:
            cur_sum = cur_sum + int(i)
        if cur_sum > max_sum:
            max_sum = cur_sum
            num_max_sum = x
if max_sum > 0:
    print(f"Число с максимальной суммой цифр - {num_max_sum}, сумма цифр равна {max_sum}")
