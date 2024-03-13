import unittest
from Stack import Stack

class TestStackMethods(unittest.TestCase):
    def test_push(self):
        """
        Test Stack can add values the top
        """
        stack = Stack()
        stack.push(4)
        stack.push(2)
        stack.push(9)
        stack.push(13)
        stack.push(16)

        self.assertEqual(stack.head.data, 4)
        self.assertEqual(stack.head.next.data, 2)
        self.assertEqual(stack.head.next.next.data, 9)
        self.assertEqual(stack.head.next.next.next.data, 13)
        self.assertEqual(stack.head.next.next.next.next.data, 16)

    def test_pop(self):
        """
        Test that Stack can remove from the top
        """
        stack = Stack()
        stack.push(4)
        stack.push(2)
        stack.push(9)
        stack.push(13)
        stack.push(16)

        # remove 16
        self.assertEqual(stack.pop(), 16)
        self.assertEqual(stack.head.next.next.next.next, None)
        
        # remove 13
        self.assertEqual(stack.pop(), 13)
        self.assertEqual(stack.head.next.next.next, None)

        # remove 9
        self.assertEqual(stack.pop(), 9)
        self.assertEqual(stack.head.next.next, None)

        # remove 2
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.head.next, None)

        # remove 4
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.head, None)

        # remove None
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self):
        """
        Test that Stack can see value from the top
        """
        stack = Stack()
        stack.push(4)
        self.assertEqual(stack.peek(), 4)

        stack.push(2)
        stack.push(9)

        stack.push(13)
        self.assertEqual(stack.peek(), 13)

        stack.push(16)
        self.assertEqual(stack.peek(), 16)
        

    def test_isEmpty(self):
        """
        Test that Stack can verify if has values
        """
        stack = Stack()
        self.assertTrue(stack.isEmpty())

        stack.push(4)
        self.assertFalse(stack.isEmpty())

        stack.pop()
        self.assertTrue(stack.isEmpty())

        stack.push(13)
        self.assertFalse(stack.isEmpty())

    def test_size(self):
        """
        Test that Stack can verify it size 
        """
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(13)
        self.assertEqual(stack.size(), 1)
        stack.push(26)
        stack.push(42)
        stack.push(98)
        stack.push(76)
        stack.push(12)
        self.assertEqual(stack.size(), 6)
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertEqual(stack.size(), 2)

if __name__ == "__main__":
    unittest.main()
