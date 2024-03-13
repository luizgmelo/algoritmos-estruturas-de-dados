import unittest
from Queue import Queue

class TestQueueMethos(unittest.TestCase):
    def test_enqueue(self):
        my_queue = Queue()
        my_queue.enqueue(5)
        my_queue.enqueue(10)
        my_queue.enqueue(15)
        self.assertEqual(my_queue.head.data, 5)
        self.assertEqual(my_queue.head.next.data, 10)
        self.assertEqual(my_queue.head.next.next.data, 15)

    def test_dequeue(self):
        my_queue = Queue()
        my_queue.enqueue(5)
        my_queue.enqueue(10)
        my_queue.enqueue(15)

        # 5 -> 10 -> 15 -> None
        my_queue.dequeue()
        # 10 -> 15 -> None
        self.assertEqual(my_queue.head.data, 10)
        my_queue.dequeue()
        # 15 -> None
        self.assertEqual(my_queue.head.data, 15)
        my_queue.dequeue()
        # None
        self.assertEqual(my_queue.head, None)
        
        my_queue.dequeue()
        # None
        self.assertEqual(my_queue.head, None)

    def test_isEmpty(self):
        my_queue = Queue()
        self.assertEqual(my_queue.isEmpty(), True)
        my_queue.enqueue(20)
        self.assertEqual(my_queue.isEmpty(), False)
        my_queue.dequeue()
        self.assertEqual(my_queue.isEmpty(), True)

    def test_size(self):
        my_queue = Queue()
        self.assertEqual(my_queue.size(), 0)
        my_queue.enqueue(20)
        self.assertEqual(my_queue.size(), 1)
        my_queue.enqueue(15)
        my_queue.enqueue(10)
        self.assertEqual(my_queue.size(), 3)

        my_queue.dequeue()
        my_queue.dequeue()
        self.assertEqual(my_queue.size(), 1)
        my_queue.dequeue()
        self.assertEqual(my_queue.size(), 0)



