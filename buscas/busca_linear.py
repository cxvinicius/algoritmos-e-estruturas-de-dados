def busca_linear(lista, valor):
    for indice, numero in enumerate(lista):
        if valor == numero:
            return indice
    return -1


lista_inteiros = [2, 6, 10, 15, 25, 40]
result = busca_linear(lista_inteiros, 2)
print(result)


