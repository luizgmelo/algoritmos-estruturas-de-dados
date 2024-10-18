class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    
    def add_to_end(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove_from_front(self):
        if self.head is None:
            return
        removed_value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        return removed_value

    def remove_from_end(self):
        if self.tail is None:
            return
        removed_value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        return removed_value

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ") 
            current = current.next
        print("None")



linked_list = LinkedList()
# Test adding to front
print("Adding to front:")
linked_list.add_to_front(10)
linked_list.add_to_front(20)
linked_list.add_to_front(30)
linked_list.print_list()  # Expected: 30 -> 20 -> 10 -> None

# Test adding to end
print("\nAdding to end:")
linked_list.add_to_end(40)
linked_list.add_to_end(50)
linked_list.print_list()  # Expected: 30 -> 20 -> 10 -> 40 -> 50 -> None

# Test removing from front
print("\nRemoving from front:")
removed = linked_list.remove_from_front()
print(f"Removed: {removed}")
linked_list.print_list()  # Expected: 20 -> 10 -> 40 -> 50 -> None

# Test removing from end
print("\nRemoving from end:")
removed = linked_list.remove_from_end()
print(f"Removed: {removed}")
linked_list.print_list()  # Expected: 20 -> 10 -> 40 -> None