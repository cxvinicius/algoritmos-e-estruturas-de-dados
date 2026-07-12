def busca_binaria(lista, valor):
    left = 0
    right = len(lista) - 1
  

    while left <= right:
        mid  = (left + right) // 2

        if lista[mid] == valor:
            return mid
        
        elif lista[mid] > valor:
            right = mid - 1
        
        else:
            left = mid + 1
    
    return -1


lista_inteiros = [2, 6, 10, 15, 25, 40, 50]
result = busca_binaria(lista_inteiros, 25)
print(result)
