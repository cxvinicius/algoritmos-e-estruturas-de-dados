from hash_table import HashTable

tabela = HashTable(5)

tabela.inserir("Caio", 22)
tabela.inserir("Vinicius", 25)
tabela.inserir("Pedro", 31)
print(tabela.tabela)

print("=== BUSCA ===")
print(tabela.buscar("Caio"))
print(tabela.buscar("Vinicius"))
print(tabela.buscar("Pedro"))

print("\n=== BUSCA INEXISTENTE ===")
print(tabela.buscar("Lucas"))

print("\n=== REMOÇÃO ===")
print(tabela.remover("Caio"))
print(tabela.buscar("Caio"))
print(tabela.remover("Carlos"))

print("\n=== ATUALIZAÇÃO ===")
tabela.inserir("Vinicius", 60)
print(tabela.buscar("Vinicius"))

print(tabela.tabela)


