import unittest
from avl import AVL, Node

class TestAVLMethods(unittest.TestCase):
    def test_left_rotate(self):
        avl = AVL()
        avl.root = Node(1)
        avl.root.right = Node(2)
        avl.root.right.right = Node(3)
        avl.root.right.parent = avl.root
        avl.root.right.right.parent = avl.root.right
        avl.root = avl.left_rotate(avl.root)
        self.assertEqual(avl.root.data, 2)
        self.assertEqual(avl.root.left.data, 1)
        self.assertEqual(avl.root.right.data, 3)

        # parents
        self.assertEqual(avl.root.parent, None)
        self.assertEqual(avl.root.left.parent, avl.root)
        self.assertEqual(avl.root.right.parent, avl.root)

    def test_right_rotate(self):
        avl = AVL()
        avl.root = Node(3)
        avl.root.left = Node(2)
        avl.root.left.left = Node(1)
        avl.root.left.parent = avl.root
        avl.root.left.left.parent = avl.root.left
        avl.root = avl.right_rotate(avl.root)
        self.assertEqual(avl.root.data, 2)
        self.assertEqual(avl.root.left.data, 1)
        self.assertEqual(avl.root.right.data, 3)

        # parents
        self.assertEqual(avl.root.parent, None)
        self.assertEqual(avl.root.left.parent, avl.root)
        self.assertEqual(avl.root.right.parent, avl.root)

    def test_double_left_rotate(self):
        avl = AVL()
        avl.root = Node(1)
        avl.root.right = Node(3)
        avl.root.right.left = Node(2)
        avl.root.right.parent = avl.root
        avl.root.right.left.parent = avl.root.right
        avl.root = avl.double_left_rotate(avl.root)
        self.assertEqual(avl.root.data, 2)
        self.assertEqual(avl.root.left.data, 1)
        self.assertEqual(avl.root.right.data, 3)

        # parents
        self.assertEqual(avl.root.parent, None)
        self.assertEqual(avl.root.left.parent, avl.root)
        self.assertEqual(avl.root.right.parent, avl.root)

    def test_double_right_rotate(self):
        avl = AVL()
        avl.root = Node(3)
        avl.root.left = Node(1)
        avl.root.left.right = Node(2)
        avl.root.left.parent = avl.root
        avl.root.left.right.parent = avl.root.left
        avl.root = avl.double_right_rotate(avl.root)
        self.assertEqual(avl.root.data, 2)
        self.assertEqual(avl.root.left.data, 1)
        self.assertEqual(avl.root.right.data, 3)

        # parents
        self.assertEqual(avl.root.parent, None)
        self.assertEqual(avl.root.left.parent, avl.root)
        self.assertEqual(avl.root.right.parent, avl.root)

    def test_get_height(self):
        avl = AVL()
        avl.root = Node(43)
        self.assertEqual(avl.get_height(avl.root), 0)
        avl.root.left = Node(22)
        self.assertEqual(avl.get_height(avl.root), 1)
        self.assertEqual(avl.get_height(avl.root.left), 0)

    def test_insert(self):
        avl = AVL()
        avl.insert(43)
        avl.insert(22)
        avl.insert(81)
        avl.insert(12)
        avl.insert(33)
        avl.insert(70)
        avl.insert(92)
        self.assertEqual(avl.root.data, 43)
        self.assertEqual(avl.root.left.data, 22)
        self.assertEqual(avl.root.right.data, 81)
        self.assertEqual(avl.root.left.left.data, 12)
        self.assertEqual(avl.root.left.right.data, 33)
        self.assertEqual(avl.root.right.left.data, 70)
        self.assertEqual(avl.root.right.right.data, 92)

        # parents
        self.assertEqual(avl.root.parent, None)
        self.assertEqual(avl.root.left.parent.data, 43)
        self.assertEqual(avl.root.right.parent.data, 43)
        self.assertEqual(avl.root.left.left.parent.data, 22)
        self.assertEqual(avl.root.left.right.parent.data, 22)
        self.assertEqual(avl.root.right.left.parent.data, 81)
        self.assertEqual(avl.root.right.right.parent.data, 81)

    def test_search(self):
        avl = AVL()
        avl.insert(22)
        avl.insert(13)
        avl.insert(42)
        avl.insert(59)
        avl.insert(23)
        self.assertEqual(avl.search(avl.root, 22), True)
        self.assertEqual(avl.search(avl.root, 23), True)
        self.assertEqual(avl.search(avl.root, 42), True)
        self.assertEqual(avl.search(avl.root, 2), False)
        self.assertEqual(avl.search(avl.root, 88), False)
        self.assertEqual(avl.search(avl.root, 999), False)

    def test_min_node(self):
        avl = AVL()
        avl.insert(22)
        avl.insert(13)
        avl.insert(42)
        avl.insert(59)
        avl.insert(23)
        self.assertEqual(avl.min().data, 13)

    def test_sucessor(self):
        avl = AVL()
        avl.insert(22)
        avl.insert(13)
        avl.insert(42)
        avl.insert(23)
        # suc 22
        self.assertEqual(avl.sucessor(avl.root).data, 23)
        # suc 42
        self.assertEqual(avl.sucessor(avl.root.right), None)
        # suc 13
        self.assertEqual(avl.sucessor(avl.root.left).data, 22)
        # suc 23
        self.assertEqual(avl.sucessor(avl.root.right.left).data, 42)

    def test_delete(self):
        # delete a leaf is a root
        avl = AVL()
        avl.root = Node(5)
        avl.delete(5)
        self.assertEqual(avl.root, None)

        # delete a leaf is left child
        avl = AVL()
        avl.root = Node(5)
        avl.root.left = Node(2)
        avl.root.left.parent = avl.root
        avl.delete(2)
        self.assertEqual(avl.root.left, None)

        # delete a leaf is right child
        avl = AVL()
        avl.root = Node(5)
        avl.root.right = Node(10)
        avl.root.right.parent = avl.root
        avl.delete(10)
        self.assertEqual(avl.root.right, None)
        
        # delete with only a single left child
        avl = AVL()
        avl.insert(25)
        avl.insert(30)
        avl.insert(10)
        avl.insert(5)
        avl.delete(10)
        self.assertEqual(avl.root.left.data, 5)

        # delete with only a single right child
        avl = AVL()
        avl.insert(25)
        avl.insert(10)
        avl.insert(30)
        avl.insert(35)
        avl.delete(30)
        self.assertEqual(avl.root.right.data, 35)
        

        # delete with two children
        avl = AVL()
        avl.insert(25)
        avl.insert(10)
        avl.insert(30)
        avl.insert(8)
        avl.insert(15)
        avl.delete(10)
        self.assertEqual(avl.root.left.data, avl.sucessor(avl.root.left).data)



    
