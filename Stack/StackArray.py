class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        return self.items.append(value)

    def pop(self):
        if not len(self.items):
            raise IndexError("Empty stack")
        return self.items.pop()

    def peek(self):
        if not len(self.items):
            raise IndexError("Empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Peek",stack.peek()) # 3
print(stack.pop()) # 3
print("Peek",stack.peek()) # 2
print(stack.pop()) # 2
print(stack.pop()) # 1
stack.pop() # Raise Empty Stack