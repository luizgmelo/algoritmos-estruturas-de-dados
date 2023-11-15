import unittest
from random import shuffle
from MinHeap import MinHeap



class TestMinHeap(unittest.TestCase):
    def test_insert(self):
        # 10 5 3
        """
            2
        10      5
        """
        test_heap = MinHeap()
        test_heap.insert(10)
        test_heap.insert(5)
        test_heap.insert(2)
        self.assertEqual(test_heap.root.value, 2)
        self.assertEqual(test_heap.root.left.value, 10)
        self.assertEqual(test_heap.root.right.value, 5)
        # 2 5 10
        """
            2
        5      10
        """
        test_heap = MinHeap()
        test_heap.insert(2)
        test_heap.insert(5)
        test_heap.insert(10)
        self.assertEqual(test_heap.root.value, 2)
        self.assertEqual(test_heap.root.left.value, 5)
        self.assertEqual(test_heap.root.right.value, 10)
        # 5 2 10
        """
            2
        5       10
        """
        test_heap = MinHeap()
        test_heap.insert(5)
        test_heap.insert(2)
        test_heap.insert(10)
        self.assertEqual(test_heap.root.value, 2)
        self.assertEqual(test_heap.root.left.value, 5)
        self.assertEqual(test_heap.root.right.value, 10)

    def test_remove(self):
        test_heap = MinHeap()
        test_heap.insert(5)
        test_heap.insert(10)
        test_heap.insert(7)
        test_heap.insert(3)
        test_heap.insert(8)
        test_heap.insert(9)
        test_heap.insert(2)
        test_heap.insert(6)
        test_heap.insert(1)
        test_heap.insert(4)
        test_heap.insert(0)
        for i in range(0, 11):
            self.assertEqual(test_heap.remove(), i)

        test_heap = MinHeap()
        numbers = [i for i in range(0, 50)]
        shuffle(numbers)
        for value in numbers:
            test_heap.insert(value)
        for i in range(0, 50):
            self.assertEqual(test_heap.remove(), i)

    def test_last(self):
        test_heap = MinHeap()
        test_heap.insert(10)
        test_heap.insert(5)
        test_heap.insert(2)
        self.assertEqual(test_heap.last.value, 5)





if __name__ == '__main__':
    unittest.main()