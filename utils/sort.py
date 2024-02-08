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
    if len(vector) <= 1:
        return vector
    mitad = len(vector) // 2
    izq = merge_sort(vector[:mitad])
    der = merge_sort(vector[mitad:])
    return merge(izq, der)
def merge (izq, der):
    i, j= 0, 0
    merged= []

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            merged.append(izq[i])
            i+=1
        else:
            merged.append(der[j])
    merged.extend(izq[i:])
    merged.extend(der[j:])

    return merged