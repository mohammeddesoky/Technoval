queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
item = queue.pop(0)
print(item)
print(queue)

###### Another Solution with dequeue #####
### deque preferred for queues because Time Complexity in deque is O(1) But in List is O(n)
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue.popleft())  # 10
print(len(queue))

###### Another Way (from Scratch) #####
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())