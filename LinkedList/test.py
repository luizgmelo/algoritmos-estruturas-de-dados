import unittest

from Linked_list import LinkedList

class TestLinkedList(unittest.TestCase):


  def test_list_insert(self):
    my_list = LinkedList()
    my_list.insert(0, 1)
    self.assertEqual(my_list.head.data, 1)
    my_list.insert(1, 2)
    self.assertEqual(my_list.head.next.data, 2)
    my_list.insert(2, 3)
    self.assertEqual(my_list.head.next.next.data, 3)
    my_list.insert(1, 4)
    self.assertEqual(my_list.head.next.data, 4)
    self.assertEqual(len(my_list), 4)

  def test_getitem(self):
    my_list = LinkedList()
    my_list.insert(0, 1)
    my_list.insert(1, 4)
    my_list.insert(2, 9)
    my_list.insert(3, 5)
    self.assertEqual(my_list[0], 1)
    self.assertEqual(my_list[1], 4)
    self.assertEqual(my_list[2], 9)
    self.assertEqual(my_list[3], 5)
    self.assertEqual(my_list[-1], 5)

  def test_list_len(self):
    my_list = LinkedList()
    my_list.insert(0, 3)
    my_list.insert(1, 8)
    self.assertEqual(len(my_list), 2)

  def test_insert_at_end(self):
    my_list = LinkedList()
    my_list.insertAtEnd(1)
    self.assertEqual(my_list[-1], 1)
    my_list.insertAtEnd(3)
    my_list.insertAtEnd(9)
    self.assertEqual(my_list[-1], 9)
    my_list.insertAtEnd(4)
    self.assertEqual(my_list[-1], 4)
    self.assertEqual(len(my_list), 4)

  def test_list_clear(self):
    my_list = LinkedList()
    my_list.insert(0, 1)
    my_list.insert(1, 3)
    my_list.insert(2, 6)
    my_list.insert(3, 9)
    my_list.clear()
    self.assertEqual(len(my_list), 0)
    self.assertEqual(my_list.head, None)
    self.assertEqual(my_list.count, 0)

  def test_list_index(self):
    my_list = LinkedList()
    my_list.insert(0, 1)
    my_list.insert(1, 3)
    my_list.insert(2, 6)
    my_list.insert(3, 9)
    self.assertEqual(my_list.index(1), 0)
    self.assertEqual(my_list.index(3), 1)
    self.assertEqual(my_list.index(6), 2)
    self.assertEqual(my_list.index(9), 3)
    with self.assertRaises(ValueError):
      my_list.index(999)
    with self.assertRaises(ValueError):
      my_list.index(-999)

if __name__ == "__main__":

  unittest.main()
