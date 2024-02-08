def shell_sort(vector):
    distancia= len(vector)//2
    while distancia > 0:
        for i in range(distancia,len(vector)):
            aux= vector[i]
            while i >= distancia and vector[i-distancia] > aux:
                vector[i]=vector[i-distancia]
                i -= distancia
            vector[i]=aux
        distancia = distancia//2
    return vector

def quick_sort(vector):
    if len(vector)<=1:
        return vector

    pivote = vector[0]
    mayores=[]
    menores=[]
    for i in range(1, len(vector)):
        if vector[i] <= pivote:
            menores.append(vector[i])
        else:
            mayores.append(vector[i])

    lista_ordenada = quick_sort(menores)
    lista_ordenada.extend([pivote])
    lista_ordenada.extend(quick_sort(mayores))
    return lista_ordenada
    return vector

def mezcla (arr_l,arr_r):
    arr_solucion=[]
    while len(arr_l) > 0 and len(arr_r)>0:
        if arr_l[0] > arr_r[0]:
            arr_solucion.append(arr_r[0])
            arr_r.pop(0)
        else:
            arr_solucion.append(arr_l[0])
            arr_l.pop(0)
    while len(arr_l) > 0:
        arr_solucion.append(arr_l[0])
        arr_l.pop(0)
    while len(arr_r) > 0:
        arr_solucion.append(arr_r[0])
        arr_r.pop(0)
    return arr_solucion
    
def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    mitad = len(vector)//2
    mitad_l= vector[:mitad]
    mitad_r= vector[mitad:]
    mitad_l= merge_sort(mitad_l)
    mitad_r= merge_sort(mitad_r)
    return mezcla(mitad_l,mitad_r)