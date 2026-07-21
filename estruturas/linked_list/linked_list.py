class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None    


    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        

    def find(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return current

            current = current.next

        return None
    

    def remove(self, data):
        if self.head is None:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            return True
        
        previous = self.head
        current = self.head.next

        while current is not None:
            if current.data == data:
                previous.next = current.next
                return True
            
            previous = current
            current = current.next
        
        return False
    

    def __len__(self):

        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next
        
        return counter
    
    
    def __str__(self):
        if self.head is None:
            return "None"
        
        result = []
        current = self.head

        while current is not None:
            result.append(str(current.data))
            current = current.next

        return " -> ".join(result) + " -> None"
        

