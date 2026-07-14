from hash_table import HashTable

estoque = HashTable(7)

estoque.inserir("PC001", "Notebook")
estoque.inserir("PC002", "Monitor Curvo")
estoque.inserir("PC003", "Mouse Claw Grip")
estoque.inserir("PC004", "Teclado Mecânico")
estoque.inserir("PC005", "Headset Gamer")

print("=== BUSCA ===")
print(estoque.buscar("PC001"))
print(estoque.buscar("PC0010"))


print("\n=== ATUALIZAÇÃO ===")
estoque.inserir("PC003", "Mouse Logitech")
print(estoque.buscar("PC003"))

print("\n=== REMOÇÃO ===")
print(estoque.remover("PC005"))
print(estoque.buscar("PC005"))

print(estoque.tabela)