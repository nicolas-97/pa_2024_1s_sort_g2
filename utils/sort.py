import utils.functions as functions


def shell_sort(vector):
    if not functions.validate_size(vector):
        return vector

    size_vector = len(vector)
    split_size = size_vector // 2

    while split_size > 0:
        for i in range(split_size, size_vector):
            value_in_position_i = vector[i]
            cycle_number = i
            while cycle_number >= split_size and vector[cycle_number - split_size] > value_in_position_i:
                vector[cycle_number] = vector[cycle_number - split_size]
                cycle_number -= split_size
                value_in_position_i = vector[cycle_number]
        split_size //= 2

    return vector


def quick_sort(vector):
    if not functions.validate_size(vector):
        return vector
    pivot = vector[0]
    lesser_value = [x for x in vector[1:] if x <= pivot]
    greater = [x for x in vector[1:] if x > pivot]
    return quick_sort(lesser_value) + [pivot] + quick_sort(greater)


def merge_sort(vector):
    if not functions.validate_size(vector):
        return vector
    if len(vector) > 1:
        middle = len(vector) // 2
        left = vector[:middle]
        right = vector[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                vector[k] = left[i]
                i += 1
            else:
                vector[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            vector[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            vector[k] = right[j]
            j += 1
            k += 1

    return vector
