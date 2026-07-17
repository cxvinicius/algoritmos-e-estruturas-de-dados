class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, valor):
        self.items.append(valor)
    
    def pop(self):
        if self.items:
            item_removido = self.items.pop(-1)
            return item_removido
        return None
    
    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    
    def is_empty(self):
        return not self.items
    
    def size(self):
        if self.items:
            return len(self.items)
      