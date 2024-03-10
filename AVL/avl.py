class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 0

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
        
        if self.root == z:
            self.root = y

        z.right = t2
        z.parent = y

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    # left-right case
    def double_left_rotate(self, z):
        z.right = self.right_rotate(z.right)
        return self.left_rotate(z)
        
    
    # left-left case
    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        y.parent = z.parent

        if self.root == z:
            self.root = y

        z.left = t3
        z.parent = y

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y
    
    # right-left case
    def double_right_rotate(self, z):
        z.left = self.left_rotate(z.left)
        return self.right_rotate(z)


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

        balance_factor = self.get_height(root.left) - self.get_height(root.right)

        if balance_factor > 1 and data < root.left.data:
            """
                3            2
               /            / \\
              2      =>    1   3
             /
            1
            """
            return self.right_rotate(root)

        if balance_factor > 1 and data > root.left.data:
            """
               3            3          2
              /    Left    /   Right  / \\
             1      =>    2     =>   1   3
              \\         /
               2        1
            """
            return self.double_right_rotate(root)

        if balance_factor < -1 and data > root.right.data:
            """
              1                2 
               \\     Left    / \\
                2      =>    1   3
                 \\
                  3
            """
            return self.left_rotate(root)

        if balance_factor < -1 and data < root.right.data:
            """
             1             1                2
              \\    Right   \\    Left     / \\
               3      =>     2     =>     1   3
              //              \\
              2                3
            """
            return self.double_left_rotate(root)

    
    def get_height(self, node):
        if (node is None) or (node.left is None and node.right is None):
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

    def search(self, root, data):
        if root is None:
            return False
        elif root.data == data:
            return True
        elif root.data > data:
            return self.search(root.left, data)
        elif root.data < data:
            return self.search(root.right, data)

    def min(self):
        if self.root is None:
            return None
        return self.__min_node(self.root)

    def __min_node(self, root):
        if root.left is None:
            return root

        return self.__min_node(root.left)

    def sucessor(self, root):
        if root is None:
            return None
        elif root.right is not None:
            return self.__min_node(root.right)
        else:
            dad = root.parent
            while (dad is not None and dad.data < root.data):
                dad = dad.parent
            return dad

    def delete(self, data):
        if self.root is None:
            return None
        self.__delete_node(self.root, data)

    def __delete_node(self, root, data):
        if root is None:
            return False

        # find the root will be remove 
        if root.data > data:
            self.__delete_node(root.left, data)
            return root
        elif root.data < data:
            self.__delete_node(root.right, data)
            return root

        # found root to be deleted

        # leaf case
        if root.left is None and root.right is None:
            if root == self.root:
                self.root = None
                return root
            else:
                if root.parent.data > root.data:
                    # is leftchild
                    root.parent.left = None
                else:
                    #is rightchild
                    root.parent.right = None

        # one child case
        elif root.left is None:
            # rightchild
            root.right.data, root.data = root.data, root.right.data
            root.right = None
        elif root.right is None:
            # leftchild
            root.left.data, root.data = root.data, root.left.data
            root.left = None
        else:
            # two child case
            sucessor = self.sucessor(root)
            root.data = sucessor.data
            self.__delete_node(sucessor, data)
       

if __name__ == "__main__":
    avl = AVL()
