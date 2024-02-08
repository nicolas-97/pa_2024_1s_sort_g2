def shell_sort(vector):
    n = len(vector)
    while n>0:
        for i in range(len(vector)):
            temp = vector[i]
            j = i
            while j >= n and vector[j - n] > temp:
                vector[j] = vector[j - n]
                j=j-n
            vector[j] = temp
        n=n//2
    return vector

def quick_sort(vector):
    if len(vector)<=1:
        return vector
    maximo = vector[0]
    left=[]
    right=[]
    for i in range(1, len(vector)):
        if vector[i] <= maximo:
            right.append(vector[i])
        else:
            left.append(vector[i])

    lista = quick_sort(right)
    lista.extend([maximo])
    lista.extend(quick_sort(left))
    return lista
    return vector

def pivote (argument,predic):
    solucion=[]
    while len(argument) > 0 and len(predic)>0:
        if argument[0] > predic[0]:
            solucion.append(predic[0])
            predic.pop(0)
        else:
            solucion.append(argument[0])
            argument.pop(0)
    while len(argument) > 0:
        solucion.append(argument[0])
        argument.pop(0)
    while len(predic) > 0:
        solucion.append(predic[0])
        predic.pop(0)
    return solucion
    
def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    middle = len(vector)//2
    mitad= vector[:middle]
    peque= vector[middle:]
    mitad= merge_sort(mitad)
    peque= merge_sort(peque)
    return pivote(mitad,peque)