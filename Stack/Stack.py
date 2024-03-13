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
        if self.head is not None:
            if self.size() == 1:
                deleted = self.head.data
                self.head = None
                self.count -= 1
                return deleted
            current = self.head
            while current.next.next is not None:
                current = current.next
            deleted = current.next.data
            current.next = None
            self.count -= 1
            return deleted
        raise IndexError("IndexError: pop from empty Stack")

if __name__ == "__main__":
    stack = Stack()

