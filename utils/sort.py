from random import randint



def shell_sort():
    from random import randint

#?  Generador de lista
def generateList ():
    lista = []
    lista = [randint (1, 10) for i in range (0 ,5 )]
    return lista

def sort(lista):
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2

















def quick_sort():
    from random import randint

#?  Generador de lista
def generateList ():
    lista = []
    lista = [randint (1, 10) for i in range (0 ,5 )]
    return lista


#? Divisiones parciales
def  dvisor (lista):
    #! primer numero como pivote
    pivote = lista[0]
    
    #! Listas auxiliares
    menores = []
    mayores = []
    
    #! Asignacion de valores
    for i in range (1, len(lista)):
        if lista[i] < pivote :
            menores.append(lista[i])
        else :
            mayores.append(lista[i])
            
    """  print (menores,"menores")
    print (mayores, "mayores")
        """
    return  menores ,  pivote , mayores

#? Recursividad 
def quick(lista):
    if len(lista) < 2 :
        return lista
    menores , pivote , mayores = dvisor(lista)
    return quick(menores) + [pivote] + quick(mayores)










def merge_sort():
    from random import randint

# Generador de lista
def generateList():
    return [randint(1, 10) for _ in range(5)]

# Función merge para combinar dos listas ordenadas
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Función de ordenamiento Merge Sort
def mergeSort(lista):
    if len(lista) <= 1:
        return lista
    
    mid = len(lista) // 2
    left = mergeSort(lista[:mid])
    right = mergeSort(lista[mid:])
    
    return merge(left, right)




print("\n")
print("Merge Sort")
lista = generateList()
print("Lista generada:", lista)
sorted_list = mergeSort(lista)
print("Lista ordenada:", sorted_list)
    
    
lista = generateList()
print("\n")
print("Quick Sort")
print (f"La lista original es {lista}")
print ("La lista ordenada es :", quick(lista))
print("\n")



print("Shell Sort")
lista = generateList()
print ( "Lista original : ",lista)
sort(lista)
print("Lista ordenada:", lista) 
