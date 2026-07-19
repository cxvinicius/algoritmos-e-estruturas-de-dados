from estruturas.queue.queue_structure import Queue

fila = Queue()

clientes = [
    "Carlos",
    "Maria",
    "João",
    "Fernanda",
    "Lucas"
]

for cliente in clientes:
    fila.enqueue(cliente)

print("\n===== FILA DE ATENDIMENTO =====")
print(fila)

print(f"\nPróximo cliente: {fila.peek()}")

print(f"\nQuantidade de clientes: {len(fila)}")

print(f"\nCliente atendido: {fila.dequeue()}")

fila.enqueue("Amanda")

print(f"\nCliente atendido: {fila.dequeue()}")
print(f"\nCliente atendido: {fila.dequeue()}")

print("\n===== FILA ATUAL =====")
print(fila)
print("========================")
print(f"\nPróximo cliente: {fila.peek()}")
print(f"\nQuantidade de clientes: {len(fila)}")
print(f"\nA fila esta vazia: {fila.is_empty()}")






