class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self.__insert_node(data, self.root)

    def __insert_node(self, data, root):
        if data < root.data:
            if root.left is None:
                self.root.left = Node(data)
                return
            self.__insert_node(data, root.left)
        elif data >= root.data:
            if root.right is None:
                self.root.right = Node(data)
                return
            self.__insert_node(data, root.right)

    def print_inoder(self, root):
        if root is not None:
            self.print_inoder(root.left)
            print(root.data, end=" ")
            self.print_inoder(root.right)

    def print_preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.print_inoder(root.left)
            self.print_inoder(root.right)

    def print_postorder(self, root):
        if root is not None:
            self.print_inoder(root.left)
            self.print_inoder(root.right)
            print(root.data, end=" ")

if __name__ == "__main__":
    avl = AVL()
    avl.insert(2)
    avl.insert(1)
    avl.insert(3)
    avl.print_inoder(avl.root)
    print("INORDER")
    avl.print_preorder(avl.root)
    print("PREORDER")
    avl.print_postorder(avl.root)
    print("POST")
