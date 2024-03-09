class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None
    
    # ref rotations: https://www.geeksforgeeks.org/insertion-in-an-avl-tree/

    # right-right case
    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        y.parent = z.parent

        z.right = t2
        z.parent = y

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    # left-right case
    def double_left_rotate(self, z):
        pass
        
    
    # left-left case
    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        y.parent = z.parent

        z.left = t3
        z.parent = y

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y
    
    # right-left case
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
                root.left = Node(data)
                root.left.parent = root
            else:
                self.__insert_node(data, root.left)
        elif data >= root.data:
            if root.right is None:
                root.right = Node(data)
                root.right.parent = root
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
            self.print_preorder(root.left)
            self.print_preorder(root.right)

    def print_postorder(self, root):
        if root is not None:
            self.print_postorder(root.left)
            self.print_postorder(root.right)
            print(root.data, end=" ")

if __name__ == "__main__":
    avl = AVL()
