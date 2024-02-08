def shell_sort(vector):
    numero = len(vector)
    br = numero // 2

    while br > 0:
        for i in range(br, numero):
            temp = vector[i]
            j = i

            while j >= br and vector[j - br] > temp:
                vector[j] = vector[j - br]
                j -= br

            vector[j] = temp

        br //= 2
    return vector



def quick_sort(vector):
    if len(vector) < 1:
        return vector
    pivote = vector[0]
    izquierda = [x for x in vector if x < pivote]
    derecha = [x for x in vector if x > pivote]
    mitad = [x for x in vector if x == pivote]

    return quick_sort(izquierda) + mitad + quick_sort(derecha)


def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    
    mitad = len(vector) // 2
    izquierda = merge_sort(vector[:mitad])
    derecha = merge_sort(vector[mitad:])

    return merge(izquierda, derecha)


def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


