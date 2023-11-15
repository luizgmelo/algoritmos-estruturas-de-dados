class MinHeap:
    class Node:
        def __init__(self, value, left = None, right = None, parent = None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent

        def __str__(self):
            return f'{self.value}'

    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self, queue=None, visited=None):
        if self.root is None:
            return ''
        if queue is None:
            queue = [self.root]
            visited = f'{self.root}'
        first = queue.pop(0)

        if not first.left:
            return visited
        visited += f' {first.left.value}'
        if not first.right:
            return visited
        visited += f' {first.right.value}'

        queue.append(first.left)               
        queue.append(first.right)
        return self.__str__(queue, visited)
        
    def __heapify_up(self, inserted):
        if inserted.parent is None:
            return
        if inserted.parent.value > inserted.value:
            inserted.parent.value, inserted.value = inserted.value, inserted.parent.value
        self.__heapify_up(inserted.parent)

    def insert(self, value):
        new_node = self.Node(value)
        self.size += 1
        if self.root is None:
            self.root = new_node
            return
        return self.__insert(value)

    def __insert(self, value, queue=None):
        if queue is None:
            queue = [self.root]

        first = queue.pop(0)

        if not first.left:
            first.left = self.Node(value)
            first.left.parent = first
            self.__heapify_up(first.left)
            return
        if not first.right:
            first.right = self.Node(value)
            first.right.parent = first
            self.__heapify_up(first.right)
            return
        queue.append(first.left)
        queue.append(first.right)
        self.__insert(value, queue)

    @property
    def last(self):
        queue = [self.root]
        while len(queue) > 0:
            last = queue.pop(0)

            if last.left:
                queue.append(last.left)

            if last.right:
                queue.append(last.right)
        return last

    def __heapify_down(self, root):
        if root.left and root.right:
            if root.left.value < root.right.value:
                if root.value > root.left.value:
                    root.left.value, root.value = root.value, root.left.value
                    self.__heapify_down(root.left)
        if root.right and root.value > root.right.value:
            root.right.value, root.value = root.value, root.right.value
            self.__heapify_down(root.right)

    def remove(self):
        if self.root is None:
            raise Exception("Heap is empty")
        if self.size == 1:
            removed = self.root.value
            self.root = None
            return removed
        removed = self.root.value
        self.root.value = self.last.value

        if self.last.parent.left == self.last:
            self.last.parent.left = None
        else:
            self.last.parent.right = None

        self.__heapify_down(self.root)
        self.size -= 1
        return removed


if __name__ == "__main__":
    heap = MinHeap()
