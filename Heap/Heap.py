class MinHeap:
    def __init__(self):
        self.heap = []

    def left_children(self, i):
        return i * 2 + 1
        
    def right_children(self, i):
        return i * 2 + 2
    
    def parent(self, i):
        return (i-1) // 2
    
    def heapify_up(self, index):
        if index == 0:
            return

        parent_index = self.parent(index)

        if self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index] 
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        size = len(self.heap)

        min_index = index
        left = self.left_children(min_index)
        right = self.right_children(min_index)

        if left < size and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < size and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self.heapify_down(min_index)
        
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) -1)
    
    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()

        root = 0
        popped_value = self.heap[root]
        self.heap[root] = self.heap.pop()
        self.heapify_down(0)

        return popped_value

    def display(self):
        print(self.heap)

heap = MinHeap()
heap.insert(0)
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(0)

heap.display()

print(heap.extract_min()) # 0
print(heap.extract_min()) # 0
print(heap.extract_min()) # 1
print(heap.extract_min()) # 2
print(heap.extract_min()) # 3
print(heap.extract_min()) # 4
print(heap.extract_min()) # 5
heap.extract_min() # Raise Index Error
