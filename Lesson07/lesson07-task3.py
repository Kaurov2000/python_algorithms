import random

m = int(input("Введите m: "))

SIZE = 2 * m + 1
MIN = -10
MAX = 10
array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print("Изначальный массив: ", array)

def mediana(array):
    prev_pivot = None
    pivot = array[(len(array) // 2)]
    while pivot != prev_pivot:
        i = 0
        j = len(array) - 1
        while i <= j:
            while array[i] < pivot:
                i = i + 1
            while array[j] > pivot:
                j = j - 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        prev_pivot = pivot
        pivot = array[(len(array) // 2)]

mediana(array)
print("Преобразованный массив: ", array)
print("Медиана", array[m])