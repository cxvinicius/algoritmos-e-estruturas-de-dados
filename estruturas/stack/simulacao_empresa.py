from stack import Stack

caixas = Stack()

print("\n=== INSERINDO ===")
caixas.push("CX-001")
caixas.push("CX-002")
caixas.push("CX-003")
caixas.push("CX-004")
print(f"Caixas na pilha: {caixas.items}")
print(f"Caixa do topo: {caixas.peek()}")

print("\n=== REMOÇÃO ===")
print(f"Caixa retirada: {caixas.pop()}")
print(f"Caixa retirada: {caixas.pop()}")
print(f"Caixas na pilha: {caixas.items}")

print("\n=== VERIFICAÇÃO ===")
print(f"Nenhuma caixa: {caixas.is_empty()}")
print(f"Quantidade de caixa: {caixas.size()}")

print(f"Caixa retirada: {caixas.pop()}")
print(f"Caixa retirada: {caixas.pop()}")

print(f"Quantidade de caixa: {caixas.size()}")
print(f"Nenhuma caixa: {caixas.is_empty()}")

