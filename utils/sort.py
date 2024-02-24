def shell_sort(vector):
    mitad = len(vector) // 2

    while mitad > 0:
        for i in range(mitad, len(vector)):
            valor = vector[i]
            posicion = i

            while posicion >= mitad and vector[posicion - mitad] > valor:
                vector[posicion] = vector[posicion - mitad]
                posicion = posicion - mitad

            vector[posicion] = valor

        mitad = mitad // 2

    return vector

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    else:
        pivote = vector[len(vector) // 2]

        izquierda = [j for j in vector if j < pivote]

        medio = [j for j in vector if j == pivote]

        derecha = [j for j in vector if j > pivote]

        return quick_sort(izquierda) + medio + quick_sort(derecha)


def merge_sort(vector):
    if len(vector) > 1:
        mitad = len(vector) // 2
        izquierda = vector[:mitad]
        derecha = vector[mitad:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                vector[k] = izquierda[i]
                i += 1
            else:
                vector[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            vector[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            vector[k] = derecha[j]
            j += 1
            k += 1

    return vector
