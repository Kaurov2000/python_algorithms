import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE)]
print(array)
min_elem = MAX_ITEM
min_index = 0
max_elem = MIN_ITEM
max_index = SIZE - 1
i = 0
for el in array:
    if el <= min_elem:
        min_elem = el
        min_index = i
    elif el >= max_elem:
        max_elem = el
        max_index = i
    i = i + 1
if max_index == min_index:
    print("Массив состоит из одинаковых элементов")
else:
    sum_elem = 0
    sign = int ((max_index - min_index) / abs(max_index - min_index))
    i = min_index + (1 * sign)
    while i != max_index:
        sum_elem = sum_elem + array[i]
        i = i + (1 * sign)
    print(f"The sum of elements between max element {max_elem} and min element {min_elem} is {sum_elem}")