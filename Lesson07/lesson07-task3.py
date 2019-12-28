import random

m = int(input("Введите m: "))

SIZE = 2 * m + 1
MIN = -10
MAX = 10
array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print("Изначальный массив: ", array)

def mediana(array, fst, lst):
    if fst >= lst:
        return True

    pivot = array[(len(array) // 2)]
    done = True
    i = fst
    j = lst
    while i <= j:
        while array[i] < pivot:
            i = i + 1
        while array[j] > pivot:
            j = j - 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
            if array[i] == array[j]:
                done = True
            else:
                done = False
    return done

done = False
while not done:
    mediana(array, 0, SIZE-1)
print("Преобразованный массив: ", array)
print("Медиана", array[m])