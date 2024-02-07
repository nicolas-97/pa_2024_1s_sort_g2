import array


def shell_sort(vector: array) -> list:
    """

    :param vector:
    :return:
    """
    # Obtenemos la longitud del vector
    n = len(vector)

    # Obtenemos la distancia inicial
    gap = n // 2

    # Creamos un bucle según las distancias
    while gap > 0:
        # Utilizamos el Insertionsort para ordenar los elementos
        for i in range(gap, n):
            # Almacenamos el valor actual para comparar
            temp = vector[i]

            # Almacenamos el indice actual
            j = i

            # Creamos un bucle para comparar los elementos
            while j >= gap and vector[j - gap] > temp:
                # Intercambiamos los valores
                vector[j] = vector[j - gap]

                # Disminuimos el indice
                j -= gap

            # Intercambiamos los valores
            vector[j] = temp
        gap //= 2  #Acotamos la distancia nuevamente y continua el ciclo
    return vector

def quick_sort(vector: array) -> list:
    """

    :param vector:
    :return:
    """
    # Comprobamos si el vector tiene más de un elemento
    if len(vector) <= 1:
        return vector

    # Obtenemos el pivote
    pivot = vector[len(vector) // 2]

    # Obtenemos los elementos menores que el pivote
    less = [i for i in vector if i < pivot]

    # Obtenemos los elementos iguales al pivote
    equal = [i for i in vector if i == pivot]

    # Obtenemos los elementos mayores que el pivote
    greater = [i for i in vector if i > pivot]

    # Llamamos recursivamente a la función
    return quick_sort(less) + equal + quick_sort(greater)

def merge_sort(vector: array) -> list:
    """

    :param vector:
    :return:
    """
    # Comprobamos si el vector tiene más de un elemento
    if len(vector) > 1:
        # Obtenemos el punto medio
        mid = len(vector) // 2

        # Dividimos el vector en dos partes
        left_half = vector[:mid]
        right_half = vector[mid:]

        # Llamamos recursivamente a la función
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializamos los contadores
        i, j, k = 0, 0, 0

        # Creamos un bucle para comparar los elementos
        while i < len(left_half) and j < len(right_half):

            # Comparamos los elementos y los ordenamos
            if left_half[i] < right_half[j]:

                # Intercambiamos los valores si el elemento de la izquierda es menor que el de la derecha
                vector[k] = left_half[i]
                i += 1

            # Si el elemento de la derecha es menor que el de la izquierda lo intercambiamos
            else:
                vector[k] = right_half[j]
                j += 1
            k += 1

        # Comprobamos si quedan elementos
        while i < len(left_half):
            # Intercambiamos los valores si quedan elementos en la izquierda y no en la derecha
            vector[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            # Intercambiamos los valores si quedan elementos en la derecha y no en la izquierda
            vector[k] = right_half[j]
            j += 1
            k += 1
    return vector