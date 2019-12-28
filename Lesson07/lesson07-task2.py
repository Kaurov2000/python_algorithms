import random

SIZE = 10
MIN = 0
MAX = 50
array = [random.random() * MAX for _ in range(SIZE)]
#array = [random.randint(MIN,MAX) for _ in range(SIZE)]
print(array)

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        arr1 = [el for i, el in enumerate(array) if i < (len(array) // 2)]
        arr2 = [el for i, el in enumerate(array) if i >= (len(array) // 2)]
        sorted_arr1 = merge_sort(arr1)
        sorted_arr2 = merge_sort(arr2)
        n1 = len(sorted_arr1)
        n2 = len(sorted_arr2)
        i = 0
        j = 0
        res_array = []
        while i < n1 and j < n2:
            if sorted_arr1[i] < sorted_arr2[j]:
                res_array.append(sorted_arr1[i])
                i = i + 1
            else:
                res_array.append(sorted_arr2[j])
                j = j + 1
        if i == n1:
            res_array.extend(sorted_arr2[j:n2])
        else:
            res_array.extend(sorted_arr1[i:n1])
        return res_array

sorted_arr = merge_sort(array)
print(sorted_arr)