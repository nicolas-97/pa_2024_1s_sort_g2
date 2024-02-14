
def shell_sort(vector):
     n = len(vector)
     intervalo = n//2
     while intervalo > 0:
        for i in range(intervalo, n):
            temp = vector[i]
            j = i            
            while j >= intervalo and vector[j - intervalo] < temp:
                vector[j] = vector[j - intervalo]
                j -= intervalo
            vector[j] = temp
        intervalo //= 2
     return vector


def quick_sort(vector):

    return vector

def merge_sort(vector):
    return vector
