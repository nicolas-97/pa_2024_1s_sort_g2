def shell_sort(vector):
    g= len(vector) // 2
    while g > 0:
        for i in range(g, len(vector)):
            actual = vector[i]
            j = i
            while j >= g and vector[j - g] > actual:
                vector[j] = vector[j -g]
                j -= g
            vector[j] = actual
        g //= 2
    return vector

def quick_sort(vector):

    if len(vector) < 1:
        return vector
    pivote = vector[0]
    mayor = [x for x in vector if pivote < x]
    menor = [x for x in vector if pivote > x]
    medio = [x for x in vector if pivote == x]
    return quick_sort(menor) + medio + quick_sort(mayor)

def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector) // 2
        left = vector[:mid]
        right = vector[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
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
            vector[k]=right[j]
            j += 1
            k += 1
    return vector