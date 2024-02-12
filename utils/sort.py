def shell_sort(vector):
    if len(vector)<=1:
        return vector
    t= len(vector)
    p=1
    while p <= t:
        p= p * 3 + 1
    while p> 0:
        for i in range(p,t):
            j = i
            temp = vector[i]
            while j>=p and vector[j - p] > temp:
                vector[j]= vector[j - p]
                j = j - p
            vector[j] = temp
        p = p//3
    return vector

def quick_sort(vector):
    if len(vector)<=1:
        return(vector)
    pivot= vector[0]
    menor=[x for x in vector if x < pivot]
    mayor=[x for x in vector if x > pivot]
    igual=[x for x in vector if x == pivot]
    return quick_sort(menor) + igual + quick_sort(mayor)

def merge_sort(vector):
    if len(vector)<=1:
        return vector
    medio = len(vector)//2
    arreglo_izq = vector[:medio]
    arreglo_der = vector[medio:] 
    arreglo_izq = merge_sort(arreglo_izq)
    arreglo_der = merge_sort(arreglo_der)
    i = j = k= 0

    while i < len(arreglo_izq) and j < len(arreglo_der):
        if arreglo_izq[i] < arreglo_der[j]:
            vector[k] = arreglo_izq[i]
            i += 1
        else:
            vector[k]= arreglo_der[j]
            j+=1
        k+=1
    while i < len(arreglo_izq):
        vector[k] = arreglo_izq[i]
        i +=1
        k +=1
    while j < len(arreglo_der):
        vector[k] = arreglo_der[j]
        j +=1
        k += 1
    return vector