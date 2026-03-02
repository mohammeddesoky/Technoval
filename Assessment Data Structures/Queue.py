class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return 'Queue is Empty'
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())