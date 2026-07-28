from estruturas.queue.queue_structure import Queue
from estruturas.stack.stack import Stack

class Graph:
    def __init__(self, directed=False):
        self._adjacency = {}
        self._directed = directed


    def add_vertex(self, vertex):
        if vertex not in self._adjacency:
            self._adjacency[vertex] = set()


    def add_edge(self, source, destination):
        if source not in self._adjacency:
            self.add_vertex(source)

        if destination not in self._adjacency:
            self.add_vertex(destination)

        self._adjacency[source].add(destination)

        if not self._directed:
            self._adjacency[destination].add(source)


    def has_vertex(self,vertex):
        return vertex in self._adjacency


    def has_edge(self, source, destination):
        if source not in self._adjacency:
            return False

        return destination in self._adjacency[source]
    

    def get_neighbors(self, vertex):
        if vertex not in self._adjacency:
            return set()

        return self._adjacency[vertex].copy()


    def __len__(self):
        return len(self._adjacency)
    

    def __contains__(self, vertex):
        return self.has_vertex(vertex)


    def __str__(self):
        lines = []

        for vertex, neighbors in self._adjacency.items():
            formatted_neighbors = ", ".join(map(str, neighbors))
            lines.append(f"{vertex} -> {formatted_neighbors}")

        return "\n".join(lines)


    def breadth_first_search(self, start):
        if start not in self._adjacency:
            return []

        queue = Queue()
        visited = {start}
        order = []

        queue.enqueue(start)

        while not queue.is_empty():
            current = queue.dequeue()
            order.append(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

        return order


    def depth_first_search(self, start):
        if start not in self._adjacency:
            return []

        stack = Stack()
        visited = {start}
        order = []

        stack.push(start)

        while not stack.is_empty():
            current = stack.pop()
            order.append(current)

            for neighbor in reversed(sorted(self.get_neighbors(current))):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.push(neighbor)

        return order