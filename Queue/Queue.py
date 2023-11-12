class Queue:
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

    def enqueue(self, data):
        self.count += 1
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def dequeue(self):
        self.count -= 1
        tmp = self.head
        self.head = self.head.next
        return tmp.data

queue = Queue()

