class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None
    
    # ref rotations: https://www.geeksforgeeks.org/insertion-in-an-avl-tree/

    def left_rotate(self, z):
        pass

    def double_left_rotate(self, z):
        pass
    
    def right_rotate(self, z):
        pass

    def double_right_rotate(self, z):
        pass

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self.__insert_node(data, self.root)

    def __insert_node(self, data, root):
        if data < root.data:
            if root.left is None:
                self.root.left = Node(data)
            else:
                self.__insert_node(data, root.left)
        elif data >= root.data:
            if root.right is None:
                self.root.right = Node(data)
            else:
                self.__insert_node(data, root.right)

        root.height = self.get_height(root)

    
    def get_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.get_height(node.left)
            right_height = self.get_height(node.right)

            return max(left_height, right_height) + 1
    

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
    print("Height of tree is", avl.root.left.height)
