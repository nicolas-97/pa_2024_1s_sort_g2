from typing import List

def shell_sort(vector: List[int]) -> List[int]:
    # Gap inicial
    gap = len(vector) // 2
    # Algoritmo Shell Sort
    while gap > 0:
        for i in range(gap, len(vector)):
            temp = vector[i]
            j = i
            while j >= gap and vector[j - gap] > temp:
                vector[j] = vector[j - gap]
                j -= gap
            vector[j] = temp
        gap //= 2
    return vector

def quick_sort(vector: List[int]) -> List[int]:
    if len(vector) <= 1:
        return vector
    pivot = vector[len(vector) // 2]
    less = [i for i in vector if i < pivot]
    equal = [i for i in vector if i == pivot]
    greater = [i for i in vector if i > pivot]
    return quick_sort(less) + equal + quick_sort(greater)

def merge_sort(vector: List[int]) -> List[int]:
    if len(vector) > 1:
        mid = len(vector) // 2
        left_half = vector[:mid]
        right_half = vector[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                vector[k] = left_half[i]
                i += 1
            else:
                vector[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            vector[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            vector[k] = right_half[j]
            j += 1
            k += 1
    return vector
