class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        if self.top is None:
            raise IndexError("Empty Stack")
        popped_value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return popped_value
    
    def peek(self):
        if self.top is None:
            raise IndexError("Empty Stack")
        return self.top.value

    def size(self):
        return self._size


stack = Stack()
stack.push(5)
stack.push(3)
stack.push(8)
stack.push(9)

print(stack.peek()) # Output: 9
print(stack.pop()) # Output: 9
print(stack.pop()) # Output: 8
print(stack.size()) # Output: 2

print(stack.pop()) # Output: 3
print(stack.pop()) # Output: 5
print(stack.pop()) # Output: Raise IndexError
        