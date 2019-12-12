import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE)]
print(array)

max_elem = MIN_ITEM
max_index = SIZE + 1
i = 0
for el in array:
    if (el < 0) and (el >= max_elem):
        max_elem = el
        max_index = i
    i = i + 1
if max_index <= SIZE:
    print(f"Максимальный отрицательный элемент {max_elem} находится на позиции {max_index}")
else:
    print("Отрицательные элементы отсутствуют")