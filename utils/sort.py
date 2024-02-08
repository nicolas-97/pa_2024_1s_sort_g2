def shell_sort(vector):
    size = len(vector)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            temp = vector[i]

            j = i
            while j >= gap and vector[j - gap] > temp:
                vector[j] = vector[j - gap]
                j -= gap

            vector[j] = temp
        gap //= 2

    return vector

def quick_sort(vector):

    if len(vector) <= 1:
        return vector
    else:
        pivot = vector[len(vector) // 2]
        left = [x for x in vector if x < pivot]
        middle = [x for x in vector if x == pivot]
        right = [x for x in vector if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def merge_sort(vector):
    if len(vector) <= 1:
        return vector

    mid = len(vector) // 2
    left_half = vector[:mid]
    right_half = vector[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged