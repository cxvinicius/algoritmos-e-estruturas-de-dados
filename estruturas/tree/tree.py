class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root

        while current is not None:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return
                
                current = current.left

            elif data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    return
                
                current = current.right 

            else:
                return      


    def search(self, data):
        current = self.root

        while current is not None:
            if data == current.data:
                return True

            if data < current.data:
                if current.left is None:
                    return False
                current = current.left

            else:
                if data > current.data:
                    if current.right is None:
                        return False
                    current = current.right

        return False


    def find_min(self):
        if self.root is None:
            return None

        current = self.root

        while current.left is not None:
            current = current.left

        return current.data


    def find_max(self):
        if self.root is None:
            return None
        
        current = self.root
        
        while current.right is not None:
            current = current.right
        
        return current.data
                

    def in_order(self):
        values = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            values.append(node.data)
            traverse(node.right)

        traverse(self.root)

        return values