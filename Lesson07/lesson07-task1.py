import random

SIZE = 10
MIN = -100
MAX = 100
array = [random.randint(MIN,MAX) for _ in range(SIZE)]
print(array)

def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

def modified_bubble_sort(array):
    n = 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        n += 1



modified_bubble_sort(array)
print(array)