from random import randint

# Función de ordenamiento shell sort
def shell_sort(lista):
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
    
    return lista


# Función de ordenamiento quick sort
def quick_sort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivot = lista[0]
        less = [i for i in lista[1:] if i <= pivot]
        greater = [i for i in lista[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# Función de ordenamiento merge sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])
    return merge(left, right)

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


# Generador de lista aleatoria
def generate_list():
    return [randint(1, 10) for _ in range(5)]

print("\n")
print("Merge Sort")
lista = generate_list()
print("Lista generada:", lista)
sorted_list = merge_sort(lista)
print("Lista ordenada:", sorted_list)

print("\n")
print("Quick Sort")
lista = generate_list()
print (f"La lista original es {lista}")
print ("La lista ordenada es :", quick_sort(lista))
print("\n")

print("Shell Sort")
lista = generate_list()
print ( "Lista original : ",lista)
shell_sort(lista)
print("Lista ordenada:", lista)
