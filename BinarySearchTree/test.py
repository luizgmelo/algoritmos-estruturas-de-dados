import unittest
from BinarySearchTree import BST

class TestBSTMethods(unittest.TestCase):
    def test_insert(self):
        tree = BST()
        tree.insert(42)
        tree.insert(23)
        tree.insert(12)
        tree.insert(27)
        tree.insert(8)
        tree.insert(78)
        tree.insert(55)
        tree.insert(43)
        tree.insert(99)
        tree.insert(59)

        self.assertEqual(tree.root.value, 42)
        self.assertEqual(tree.root.left.value, 23)
        self.assertEqual(tree.root.left.left.value, 12)
        self.assertEqual(tree.root.left.right.value, 27)
        self.assertEqual(tree.root.right.value, 78)
        self.assertEqual(tree.root.right.right.value, 99)
        self.assertEqual(tree.root.right.left.value, 55)

        # parents
        self.assertEqual(tree.root.parent, None)
        self.assertEqual(tree.root.left.parent, tree.root)
        self.assertEqual(tree.root.left.parent, tree.root)
        self.assertEqual(tree.root.left.left.parent, tree.root.left)
        self.assertEqual(tree.root.right.right.parent, tree.root.right)

    def test_search(self):
        tree = BST()
        self.assertEqual(tree.search(12), None)

        tree.insert(42)
        tree.insert(23)
        tree.insert(12)
        tree.insert(27)
        tree.insert(8)
        tree.insert(78)

        self.assertTrue(tree.search(42))
        self.assertTrue(tree.search(23))
        self.assertTrue(tree.search(12))
        self.assertTrue(tree.search(27))
        self.assertTrue(tree.search(8))
        self.assertTrue(tree.search(78))

        self.assertFalse(tree.search(999))
        self.assertFalse(tree.search(840))
        self.assertFalse(tree.search(142))
        self.assertFalse(tree.search(356))

    def test_min_node(self):
        tree = BST()
        self.assertEqual(tree.min_node(), None)
        tree.insert(42)
        tree.insert(12)
        tree.insert(8)
        tree.insert(78)
        self.assertEqual(tree.min_node().value, 8)
        tree.insert(3)
        self.assertEqual(tree.min_node().value, 3)

    def test_sucessor(self):
        tree = BST()
        tree.insert(42)
        tree.insert(12)
        tree.insert(8)
        tree.insert(78)
        self.assertEqual(tree.successor(tree.root).value, 78)
        self.assertEqual(tree.successor(tree.root.left).value, 42)
        self.assertEqual(tree.successor(tree.root.left.left).value, 12)
        
        self.assertEqual(tree.successor(tree.root.right), None)

    def test_delete(self):
        tree = BST()
        # remove a leaf is root
        tree.insert(42)

        tree.delete(42)
        self.assertEqual(tree.root, None)

        tree.insert(100)
        tree.insert(20)
        tree.insert(10)
        tree.insert(30)
        tree.insert(200)
        tree.insert(150)
        tree.insert(300)

        # remove a leaf is not root
        tree.delete(300)
        self.assertEqual(tree.root.right.right, None)

        # remove node with one child
        tree.delete(200)
        self.assertEqual(tree.root.right.value, 150)
        self.assertEqual(tree.root.right.left, None)

        # remove node with two child
        tree.delete(20)
        self.assertEqual(tree.root.left.value, 30)
        self.assertEqual(tree.root.left.right, None)

        tree.delete(100)
        self.assertEqual(tree.root.value, 150)
        self.assertEqual(tree.root.right, None)

        self.assertEqual(tree.delete(998), None)

    def test_size(self):
        tree = BST()
        tree.insert(100)
        tree.insert(20)
        tree.insert(10)
        self.assertEqual(tree.size(), 3)
        tree.insert(30)
        tree.insert(200)
        tree.insert(150)
        tree.insert(300)
        self.assertEqual(tree.size(), 7)
        tree.delete(300)
        tree.delete(200)
        tree.delete(20)
        tree.delete(100)
        self.assertEqual(tree.size(), 3)

    # def test_print_inorder(self):
    #     pass

    # def test_print_preorder(self):
    #     pass

    # def test_print_postorder(self):
    #     pass
