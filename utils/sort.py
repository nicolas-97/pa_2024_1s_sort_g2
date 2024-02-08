def shell_sort(Lista):
    n=len(Lista)
    intervalo=n//2
    while intervalo > 0:
        for i in range (intervalo, n):
            temp = Lista[i]
            j=i
            while j >= intervalo and Lista[j- intervalo]>temp:
                Lista[j] = Lista[j-intervalo]
                j -= intervalo
            Lista[j]=temp
        intervalo//=2
    return Lista


def merge_sort(Lista):
    if len(Lista) > 1:
        medio = len(Lista) // 2
        izquierda = Lista[:medio]
        derecha = Lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                Lista[k] = izquierda[i]
                i += 1
            else:
                Lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            Lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            Lista[k] = derecha[j]
            j += 1
            k += 1


def quick_sort(Lista):
    if len(Lista) <= 1:
        return Lista
    else:
        pivote = Lista[0]
        menores = [x for x in Lista[1:] if x <= pivote]
        mayores = [x for x in Lista[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)


