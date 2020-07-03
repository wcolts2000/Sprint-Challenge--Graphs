class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def removeItem(self, index):
        return self.stack.pop(index)
        
    def size(self):
        return len(self.stack)

# def bft(self, starting_vertex_id): for dft switch to stack
    # Create an empty queue and enqueue the starting vertex ID
    # Create a Set to store visited vertices
    # While the queue is not empty...
        # Dequeue the first vertex
        # If that vertex has not been visited...
            # Mark it as visited...
            # Then add all of its neighbors to the back of the queue