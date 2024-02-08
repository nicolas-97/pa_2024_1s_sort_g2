def shell_sort(vector):
    n = len(vector)
    while n > 0:
        for i in range(len(vector)):
            temp = vector[i]
            j = i
            while j >= n and vector[j - n] > temp:
                vector[j] = vector[j - n]
                j = j-n
            vector[j] = temp
        n=n//2
    return vector

def quick_sort(vector):
    if len(vector)<=1:
        return vector

    pivote = vector[0]
    mayor=[]
    menor=[]
    for i in range(1, len(vector)):
        if vector[i] <= pivote:
            menor.append(vector[i])
        else:
            mayor.append(vector[i])

    lista = quick_sort(menor)
    lista.extend([pivote])
    lista.extend(quick_sort(mayor))
    return lista
    return vector
    
def mezcla (array_l,array_r):
    array_solucion=[]
    while len(array_l) > 0 and len(array_r)>0:
        if array_l[0] > array_r[0]:
            array_solucion.append(array_r[0])
            array_r.pop(0)
        else:
            array_solucion.append(array_l[0])
            array_l.pop(0)
    while len(array_l) > 0:
        array_solucion.append(array_l[0])
        array_l.pop(0)
    while len(array_r) > 0:
        array_solucion.append(array_r[0])
        array_r.pop(0)
    return array_solucion
    
def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    medio = len(vector)//2
    medio_l= vector[:medio]
    medio_r= vector[medio:]
    medio_l= merge_sort(medio_l)
    medio_r= merge_sort(medio_r)
    return mezcla(medio_l,medio_r)