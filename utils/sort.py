def shell_sort(vector):
    tamaño = len(vector)
    distancia = tamaño // 2
    while distancia > 0:
        distancia //= 2
        for x in range(distancia, tamaño):
            a = vector[x]
            while x >= distancia and vector[x - distancia] > a:
                vector[x] = vector[x - distancia]
                x -= distancia
            vector[x] = a
    return vector

def quick_sort(vector):
    izquierda = []
    centro = []
    derecha = []
    if vector:
        punto = vector[0]
        for i in vector:
            if i < punto: izquierda.append(i)
            elif i == punto: centro.append(i)
            elif i > punto: derecha.append(i)
        return quick_sort(izquierda)+centro+quick_sort(derecha)
    return vector

def merge_sort(vector):
    if len(vector) > 1:
        a= b = c = 0

        mid = len(vector)//2

        aux1 = vector[:mid]
        aux2 = vector[mid:]

        merge_sort(aux1)
        merge_sort(aux2)

        while a < len(aux1) and b < len(aux2):
            if aux1[a] < aux2[b]:
                vector[c] = aux1[a]
                a += 1
            else:
                vector[c] = aux2[b]
                b += 1
            c += 1
        while a < len(aux1):
            vector[c] = aux1[a]
            a += 1
            c += 1
        while b < len(aux2):
            vector[c] = aux2[b]
            b += 1
            c += 1
    return vector