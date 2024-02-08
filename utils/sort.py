def shell_sort(vector):
    long= len(vector)
    maximo = long//2
    while maximo > 0:
        for i in range (maximo,long):
            base = vector[i]
            j=i
            while j >= maximo and vector[j-maximo]>base :
                vector[j]= vector [j-maximo ]
                j-=maximo
            
            vector[j]=base
        maximo//=2
    return(vector)
lista = [34,56,78,22,31,20,11,9,8]
z=shell_sort(lista)
print(z)



def quick_sort(vector):
    if len(vector)<=1:
        return vector
    pivote =vector[0]
    izquierda= [x for x in vector if x < pivote]
    derecha = [x for x in vector if x > pivote]
    mitad = [x for x in vector if x == pivote]
    return quick_sort(izquierda) + mitad + quick_sort(derecha)
lista = [34,56,78,22,31,20,11,9,8]
m=quick_sort(lista)
print(m)


def merge_sort(vector):
    if  len(vector )>1:
        medio=len(vector)//2
        izquierda,derecha = vector [:medio], vector[medio:]
        merge_sort(izquierda)
        merge_sort(derecha)
        vector[:] = sorted (izquierda+derecha)
lista = [9,56,99,5,4,20,11,2,8]
merge_sort(lista)
print(lista)

