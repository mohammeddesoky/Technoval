from collections import deque
stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())

###### Another Way (from Scratch) #####
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(1)
s.push(2)
print(s.pop())