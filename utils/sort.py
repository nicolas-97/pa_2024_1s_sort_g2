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



def quick_sort(vector):
    if len(vector)<=1:
        return vector
    pivote =vector[0]
    izquierda= [x for x in vector if x < pivote]
    derecha = [x for x in vector if x > pivote]
    mitad = [x for x in vector if x == pivote]
    return quick_sort(izquierda) + mitad + quick_sort(derecha)



def merge_sort(vector):
    if  len(vector )>1:
        medio=len(vector)//2
        izquierda,derecha = vector [:medio], vector[medio:]
        merge_sort(izquierda)
        merge_sort(derecha)
        vector[:] = sorted (izquierda+derecha)
    return(vector)

