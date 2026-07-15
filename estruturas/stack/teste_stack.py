from stack import Stack

pilha = Stack()

print("\n=== INSERINDO ===")
pilha.push("10")
pilha.push("30")
pilha.push("50")
print(pilha.items)


print("\n=== REMOÇÃO ===")
print(pilha.pop())
print(pilha.items)


print("\n=== VERIFICAÇÃO ===")
print(pilha.peek())
print(pilha.is_empty())
print(pilha.size())

