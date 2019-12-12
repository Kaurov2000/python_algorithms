import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE)]
print(array)
result = [i for i in range(0,len(array)) if (array[i] % 2) == 0]
print(result)