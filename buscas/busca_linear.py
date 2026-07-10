def busca_linear(lista, valor_escolhido):
    for numeros in lista:
        if valor_escolhido == numeros:
            return valor_escolhido
        return -1
    
numeros = [2,4,5,6,7,810,34]


result = busca_linear(numeros, 1)
print(result)