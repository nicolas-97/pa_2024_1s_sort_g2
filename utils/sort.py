
def shell_sort(vector):
    if len(vector) < 2:
        return vector
    size = len(vector)
    cut = size // 2
    while cut > 0:
        for i in range(cut, size):
            shell = vector[i]
            j = i
            while j >= cut and vector[j - cut] > shell:
                vector[j] = vector[j - cut]
                j -= cut
                shell = vector[j]
        cut  //= 2
    return vector

def quick_sort(vector):
    if len(vector)<2:
        return vector

    pivot=vector[0]
    first=[x for x in vector[1:] if x<=pivot]   
    last=[x for x in vector[1:] if x>pivot] 
    vector=quick_sort(first) + [pivot] + quick_sort(last)

    return vector

def merge_sort(vector):
    if len(vector)<2:
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
