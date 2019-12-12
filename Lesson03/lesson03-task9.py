import random

SIZE_X = 5
SIZE_Y = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE_X)] for _ in range(SIZE_Y)]
print(*matrix, sep = '\n')

column_min = [MAX_ITEM for _ in range(SIZE_X)]
for line in matrix:
    for i,item in enumerate(line):
        if item <= column_min[i]:
            column_min[i] = item

max_elem = column_min[0]
for el in column_min:
    if el >= max_elem:
        max_elem = el
print(max_elem)