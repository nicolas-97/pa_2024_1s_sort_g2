def shell_sort(vector):
    largo=len(vector)
    espacio=largo//2
    while espacio>0:
        for i in range(espacio,largo):
            temp=vector[i]
            j=i
            while j>=espacio and vector[j-espacio]>temp:
                vector[j]=vector[j-espacio]
                j-=espacio
            vector[j]=temp
        espacio//=2
    return vector

def quick_sort(vector):
    valor_inicio=0
    valor_fin=len(vector)-1
    def quick(vector, inicio, final):
        if inicio < final:

            pivote = dividir(vector, inicio, final)
            quick(vector, inicio, pivote - 1)
            quick(vector, pivote + 1, final)
        return vector
        
    def dividir(vector, inicio, final):  
        pivote = vector[final]
        i = inicio - 1
            
        for j in range(inicio, final):
            if vector[j] <= pivote:
                i = i + 1  
                (vector[i], vector[j]) = (vector[j], vector[i])
        (vector[i + 1], vector[final]) = (vector[final], vector[i + 1])
        return i + 1
    return quick(vector, valor_inicio, valor_fin)

def merge_sort(vector):
    def sort(vector):
        longitud = len(vector)
        mitad = longitud//2  
        if longitud <= 1:
            return vector
        vector_izq = vector[:mitad]
        vector_der = vector[mitad:]
        vector_izq = sort(vector_izq)
        vector_der = sort(vector_der)
        return merge(vector_izq, vector_der)

    def merge(vector_izq, vector_der):
        vector_final = []
        indice_izq = 0
        indice_der = 0
        indice_vector_final = 0

        while indice_izq < len(vector_izq) and indice_der < len(vector_der):
            valor_vector_izq = vector_izq[indice_izq]
            valor_vector_der = vector_der[indice_der]
            if valor_vector_izq <= valor_vector_der:
                vector_final.append(valor_vector_izq)
                indice_izq += 1
            else:
                vector_final.append(valor_vector_der)
                indice_der += 1
            indice_vector_final += 1
    
        while indice_izq < len(vector_izq):
            vector_final.append(vector_izq[indice_izq])
            indice_izq += 1

        while indice_der < len(vector_der):
            vector_final.append(vector_der[indice_der])
            indice_der += 1
        return vector_final
    
    return sort(vector)