class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head) -> Node:
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    dummy = Node()
    tail = dummy
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    if left:
        tail.next = left
    elif right:
        tail.next = right

    return dummy.next

def merge_sort(head):
    if not head or not head.next:
        return head

    middle = find_middle(head)

    after_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(after_middle)

    sorted_list = merge(left, right)

    return sorted_list

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# 5 -> 6 -> 3 -> 8 -> 1 -> None
node_1 = Node(1)
node_8 = Node(8, next=node_1)
node_3 = Node(3, next=node_8)
node_6 = Node(6, next=node_3)
node_5 = Node(5, next=node_6)

print("Before merge sort: ", end="")
print_list(node_5)
sorted_list = merge_sort(node_5)
print("After merge sort: ", end="")
print_list(sorted_list)
# 1 -> 3 -> 5 -> 6 -> 8 -> None

