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
        if self.head is not None:
            if self.head.data == 0 and len(self) == 1:
                return '[0]'

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
        if isinstance(position, slice):
            step = position.step if position.step is not None else 1
            if step == 0:
                raise ValueError('Step cannot be zero')
            if step > 0:
                start = position.start if position.start is not None else 0
                stop = position.stop if position.stop is not None else len(self)
            if step < 0:
                start = position.start if position.start is not None else len(self) - 1
                stop = position.stop if position.stop is not None else -1

            if start < 0:
                start = start + len(self)
            if stop < 0 and position.stop is not None:
                stop = stop + len(self)

            part = LinkedList()
            if step > 0:
                i = 0
                indexes = range(start, stop, step)
                it = iter(self)
                while i < stop:
                    v = next(it)
                    if i in indexes:
                        part.insertAtEnd(v)
                    i += 1
            else:
                for i in range(start, stop, step):
                    part.insertAtEnd(self[i])
            return part

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

    def append(self, data):
        self.count += 1
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        self.tail.next = new_node
        self.tail = new_node

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(0)
    print("STRING:", str(linked_list))
