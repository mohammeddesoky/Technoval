class stack:
    def __init__(self):
        self.items = []

    def puch(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return 'Stack is Empty'
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return 'Stack is Empty'
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
s = stack()
s.puch(1)
s.puch(2)
s.puch(3)
print(s.peek())
s.pop()
print(s.peek())