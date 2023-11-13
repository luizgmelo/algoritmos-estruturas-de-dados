class LinkedList:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):
        return '[' + ", ".join([str(valor) for valor in self]) + ']'

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def index(self, data):
        current = self.head
        i = 0
        while current is not None:
            if current.data == data:
                return i
            current = current.next
            i += 1
        raise ValueError(f"Don't exist {data} in list")

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __getitem__(self, position):
        if position < 0:
            position = position + len(self)
        if position < 0 or position >= len(self):
            raise IndexError('Invalid Position')
        current = self.head
        i = 0
        while i < position:
            current = current.next
            i += 1
        return current.data

    def insert(self, position, data):
        self.count += 1
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head 
            return
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.count == 2:
                self.tail = new_node.next
        current = self.head
        i = 0
        while current.next is not None and i < position - 1:
            current = current.next
            i += 1
        if current.next is None:
            self.tail = new_node; 
        new_node.next = current.next
        current.next = new_node 

    def insertAtEnd(self, data):
        self.count += 1
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        self.tail.next = new_node
        self.tail = new_node

linked_list = LinkedList()
linked_list.insert(0, 1)
linked_list.insert(1, 2)
linked_list.insert(2, 3)
linked_list.insert(1, 4)
print(linked_list[0])
print(linked_list[1])
print(linked_list[2])
print(linked_list[3])
linked_list.insertAtEnd(5)
print("INDEX:", linked_list.index(5))
print("SIZE:", len(linked_list))
print("STRING:", str(linked_list))

for valor in linked_list:
    print(valor)
