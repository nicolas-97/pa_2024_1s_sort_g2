def shell_sort(vector):
    n = len(vector)
    m = n // 2   
    while m > 0:
        for i in range(m, n):
            temp = vector[i]
            j = i
            while j >=m and vector[j - m] > temp:
                vector[j] = vector[j - m]
                j -= m
            vector[j] = temp
        m //= 2
        
    return vector
    
def quick_sort(vector):

    if len(vector) <= 1:
        return vector
    
    pivot = vector[0]   
    menor = [i for i in vector[1:] if i <= pivot]
    mayor = [i for i in vector[1:] if i > pivot]   
    return quick_sort(menor) + [pivot] + quick_sort(mayor)

def merge_sort(vector):
    if len(vector) <= 1:
        return vector
   
    mitad = len(vector) // 2
    mitad_izq = vector[:mitad]
    mitad_der = vector[mitad:]
    
    mitad_izq_ordenada = merge_sort(mitad_izq)
    mitad_der_ordenada = merge_sort(mitad_der)
    
    return merge(mitad_izq_ordenada, mitad_der_ordenada)

def merge(izq, der):
    result = []
    izq_index, der_index = 0, 0
  
    while izq_index < len(izq) and der_index < len(der):
        if izq[izq_index] < der[der_index]:
            result.append(izq[izq_index])
            izq_index += 1
        else:
            result.append(der[der_index])
            der_index += 1

    while izq_index < len(izq):
        result.append(izq[izq_index])
        izq_index += 1
    
    while der_index < len(der):
        result.append(der[der_index])
        der_index += 1
    
    return result