from queue_structure import Queue

fila = Queue()

fila.enqueue("CX-1001")
fila.enqueue("CX-1002")
fila.enqueue("CX-1003")
fila.enqueue("CX-1004")
fila.enqueue("CX-1005")



print(fila)

fila.dequeue()
fila.dequeue()


fila.enqueue("CX-1006")
fila.enqueue("CX-1007")

print(fila)

