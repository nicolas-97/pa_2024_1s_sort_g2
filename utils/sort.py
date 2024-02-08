def shell_sort(vector):

    intervalo = len(vector)

    while intervalo > 0:
        for i in range(len(vector)):
            actual = vector[i]
            item = i
            while item >= intervalo and vector[item - intervalo] > actual:
                vector[item] = vector[item - intervalo]
                item = item - intervalo
            vector[item] = actual

        intervalo = intervalo // 2
    return vector

def quick_sort(vector):
    if len(vector)<=1:
        return vector

    primer_pivote = vector[0]
    vector_mayor=[]
    vector_menor=[]
    for i in range(1, len(vector)):
        if vector[i] <= primer_pivote:
            vector_menor.append(vector[i])
        else:
            vector_mayor.append(vector[i])

    lista_final = quick_sort(vector_menor)
    lista_final.extend([primer_pivote])
    lista_final.extend(quick_sort(vector_mayor))
    return lista_final
    return vector

def mix_vectores (vector_izquierdo,vector_derecho):
    array_final=[]
    while len(vector_izquierdo) > 0 and len(vector_derecho)>0:
        if vector_izquierdo[0] > vector_derecho[0]:
            array_final.append(vector_derecho[0])
            vector_derecho.pop(0)
        else:
            array_final.append(vector_izquierdo[0])
            vector_izquierdo.pop(0)
    while len(vector_izquierdo) > 0:
        array_final.append(vector_izquierdo[0])
        vector_izquierdo.pop(0)
    while len(vector_derecho) > 0:
        array_final.append(vector_derecho[0])
        vector_derecho.pop(0)
    return array_final
    
def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    valor_medio = len(vector)//2
    mitad_izquierda= vector[:valor_medio]
    mitad_derecha= vector[valor_medio:]
    mitad_izquierda= merge_sort(mitad_izquierda)
    mitad_derecha= merge_sort(mitad_derecha)
    return mix_vectores(mitad_izquierda,mitad_derecha)