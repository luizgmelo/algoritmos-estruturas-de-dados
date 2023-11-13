class BST:
    class Node:
        def __init__(self, value, left = None, right = None, parent = None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent

    def __init__(self):
        self.root = None
        self.length = 0

    def size(self):
        return self.length

    def insert(self, value):
        if self.root is None:
            self.length += 1
            self.root = self.Node(value)
            return
            
        return self.__insertNode(value, self.root)

    def __insertNode(self, value, root):
        if root.value > value:
            if root.left is None:
                self.length += 1
                root.left = self.Node(value)
                root.left.parent = root
                return
            return self.__insertNode(value, root.left)
        if root.value <= value:
            if root.right is None:
                self.length += 1
                root.right = self.Node(value)
                root.right.parent = root
                return
            return self.__insertNode(value, root.right)

tree = BST()
tree.insert(2)
tree.insert(3)
tree.insert(1)
print(tree.size())
