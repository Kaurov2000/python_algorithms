import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE)]
print(array)
min_elem = MAX_ITEM
min_index = 0
max_elem = MIN_ITEM
max_index = SIZE - 1
i = 0
for el in array:
    if el < min_elem:
        min_elem = el
        min_index = i
    elif el > max_elem:
        max_elem = el
        max_index = i
    i = i + 1
array[min_index] = max_elem
array[max_index] = min_elem
print(array)
