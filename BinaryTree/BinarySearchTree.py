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

    def search(self, value):
        if self.root is None:
            return

        return self.__search_node(value, self.root)

    def __search_node(self, value, root):
        if root.value > value:
            if root.left is None:
                return False
            return self.__search_node(value, root.left)
        if root.value < value:
            if root.right is None:
                return False
            return self.__search_node(value, root.right)
        
        return True



    def print_inorder(self, root):
        if root is not None:
            self.print_inorder(root.left)
            print(str(root.value) + " ->", end=' ')
            self.print_inorder(root.right)

    def print_preorder(self, root):
        if root is not None:
            print(str(root.value) + " ->", end=' ')
            self.print_preorder(root.left)
            self.print_preorder(root.right)

    def print_postorder(self, root):
        if root is not None:
            self.print_postorder(root.left)
            self.print_postorder(root.right)
            print(str(root.value) + " -> ", end=' ')
    

if __name__ == "__main__":
    tree = BST()
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    print(tree.size())
    print(tree.search(3))
    print(tree.search(1))
    print(tree.search(2))
    print(tree.search(99))
