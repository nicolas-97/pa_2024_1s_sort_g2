
def shell_sort(vector) :

   ## shell_sort
    longitudw = len(vector)

    distancia = longitudw // 2

    while distancia > 0:

        for i in range(distancia, longitudw):
            Vinicial = vector[i]
            j = i
            while j >= distancia and vector[j - distancia] > Vinicial:
                vector[j] = vector[j - distancia]
                j -= distancia
            vector[j] = Vinicial
        distancia //= 2  
    return vector



def quick_sort(vector): 

    if len(vector) <= 1:
        return vector

    pivot = vector[len(vector) // 2]
    men = [i for i in vector if i < pivot]



    ##
    igual = [i for i in vector if i == pivot]




    may = [i for i in vector if i > pivot]
    
    return quick_sort(men) + igual + quick_sort(may)




def merge_sort(vector): 
    ## Len 
    if len(vector) > 1:  # Verifica si el vector tiene más de un elemento
        medio = len(vector) // 2  # Encuentra el índice medio del vector
        M_Izq = vector[:medio]  # Divide el vector en mitades izquierda y derecha
        M_Der = vector[medio:]

        merge_sort(M_Izq)  # Llama recursivamente merge_sort para ordenar la mitad izquierda
        merge_sort(M_Der)  # Llama recursivamente merge_sort para ordenar la mitad derecha

        i, j, k = 0, 0, 0  # Inicializa índices para recorrer las mitades y el vector resultante

        while i < len(M_Izq) and j < len(M_Der):  # Combina las mitades ordenadas
            if M_Izq[i] < M_Der[j]:  # Compara los elementos de las mitades
                vector[k] = M_Izq[i]  # Si el elemento de la mitad izquierda es menor, lo coloca en el vector resultante
                i += 1
            else:
                vector[k] = M_Der[j]  # Si el elemento de la mitad derecha es menor, lo coloca en el vector resultante
                j += 1
            k += 1

        while i < len(M_Izq):  # Añade los elementos restantes de la mitad izquierda al vector resultante
            vector[k] = M_Izq[i]
            i += 1
            k += 1

        while j < len(M_Der):  # Añade los elementos restantes de la mitad derecha al vector resultante
            vector[k] = M_Der[j]
            j += 1
            k += 1
    return vector  # Devuelve el vector ordenado