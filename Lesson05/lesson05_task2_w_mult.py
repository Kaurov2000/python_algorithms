from collections import deque, defaultdict

def def_zero():
    return '0'

def hex_to_digit(x):
    if not x.isdigit():
        return ord(x) - 55
    else:
        return int(x)

def digit_to_hex(x):
    if x % 16 > 9:
        return chr(x % 16 + 55)
    else:
        return str(x % 16)

def hex_sum(first_num, second_num):
    n = max(len(first_num), len(second_num))
    in_mind = 0
    sum_rev = defaultdict(def_zero)
    for i in range(n):
        digit_1 = hex_to_digit(first_num[i])
        digit_2 = hex_to_digit(second_num[i])
        sum_ = digit_1 + digit_2 + in_mind
        in_mind = sum_ // 16
        sum_rev[i] = digit_to_hex(sum_)
    else:
        if in_mind > 0:
            sum_rev[n + 1] = digit_to_hex(in_mind)
    return sum_rev

def hex_mul(first_num, second_num):
    mul_sum = defaultdict(def_zero)
    for i in range(len(second_num)):
        mul1 = hex_to_digit(second_num[i])
        in_mind = 0
        mul_temp = defaultdict(def_zero)
        for k in range(i):
            mul_temp[k] = '0'
        for j in range(len(first_num)):
            mul2 = hex_to_digit(first_num[j])
            mul = mul1 * mul2 + in_mind
            in_mind = mul // 16
            mul_temp[j + i] = digit_to_hex(mul)
        else:
            if in_mind > 0:
                mul_temp[len(mul_temp)] = digit_to_hex(in_mind)
        mul_sum = hex_sum(mul_sum, mul_temp)
    return mul_sum

a = deque(input("Введите первое число: ").upper())
b = deque(input("Введите второе число: ").upper())

a.reverse()
b.reverse()

first_num = defaultdict(def_zero)
for k,v in enumerate(a):
    first_num[k] = v
second_num = defaultdict(def_zero)
for k,v in enumerate(b):
    second_num[k] = v

sum_rev = hex_sum(first_num, second_num)
sum_result = deque(v for v in sum_rev.values())
sum_result.reverse()
print("Сумма чисел равна: ", *sum_result,sep='')
mul_rev = hex_mul(first_num, second_num)
mul_result = deque(v for v in mul_rev.values())
mul_result.reverse()
print("Произведение чисел равно: ", *mul_result,sep='')