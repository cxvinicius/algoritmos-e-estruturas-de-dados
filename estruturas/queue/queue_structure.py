class Queue:
    def __init__(self):
        self._queue = []
    
    def enqueue(self, valor):
        self._queue.append(valor)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._queue.pop(0)
    
    def is_empty(self):
        return not self._queue
    
    def peek(self):
        if self.is_empty():
            return None
        return self._queue[0]
    
    def __len__(self):
        return len(self._queue)
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        
        total_queue = "Front -> "

        for i in self._queue:
            total_queue += str(i) + " -> "
        total_queue += "Rear"
        
        return total_queue
    
    