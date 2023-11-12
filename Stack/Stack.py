class Stack:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return True if self.count == 0 else False

    def size(self):
        return self.count

    def peek(self):
        # if self.size() == 1:
        #     return self.head.data
        current = self.head
        while current.next is not None:
            current = current.next
        return current.data

    def push(self, data):
        self.count += 1
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def pop(self):
        if self.size() == 1:
            self.head = None
            self.count -= 1
            return
        self.count -= 1
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

stack = Stack()

