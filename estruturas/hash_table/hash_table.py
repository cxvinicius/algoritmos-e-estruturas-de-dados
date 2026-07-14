class HashTable:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
    

    def funcao_hash(self, chave):
        soma = 0
        for caractere in chave:
            soma += ord(caractere)
        return soma % self.tamanho
    

    def inserir(self, chave, valor):
        indice = self.funcao_hash(chave)
        lista = self.tabela[indice]

        for i, (chave_atual, valor_atual) in enumerate(lista):
            if chave_atual == chave:
                lista[i] = (chave, valor)
                return
        
        lista.append((chave, valor))
    

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        lista = self.tabela[indice]

        for chave_atual, valor_atual in lista:
            if chave_atual == chave:
                return valor_atual
        return None
    
    def remover(self, chave):
        indice = self.funcao_hash(chave)
        lista = self.tabela[indice]

        for i, (chave_atual, valor_atual) in enumerate(lista):
            if chave_atual == chave:
                del lista[i] 
                return True
        return False

