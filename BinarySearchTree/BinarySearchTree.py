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


    def min_node(self):
        if self.root is None:
            return

        return self.__min_node(self.root)

    def __min_node(self, root):
        if root.left is None:
            return root
        return self.__min_node(root.left)


    def successor(self, root):
        if root is None:
            return
        
        # case root.right exist succ is the most left node
        if root.right is not None:
            succ = self.__min_node(root.right)
            return succ

        # case root.right don't exist we need look to up in the tree
        dad_succ = root.parent
        while (dad_succ is not None and dad_succ.value < root.value):
            dad_succ = dad_succ.parent

        return dad_succ

    def delete(self, value):
        if self.root is None:
            return 
        return self.__delete_node(value, self.root)

    def __delete_node(self, value, root):
        if root.value > value:
            if root.left is None:
                return
            return self.__delete_node(value, root.left)

        if root.value < value:
            if root.right is None:
                return
            return self.__delete_node(value, root.right)

        # found root

        # case 1: is a leaf
        if root.left is None and root.right is None:
            # leaf is root
            if root is self.root:
                self.root = None
                self.length -= 1
                return
            
            dad = root.parent

            if dad.left == root:
                dad.left = None
                self.length -= 1
                return
            elif dad.right == root:
                dad.right = None
                self.length -= 1
                return

        # case 2: is a node with one child
        if root.left is not None and root.right is None:
            # has leftchild
            root.left.value, root.value = root.value, root.left.value
            root.left = None
            self.length -= 1
            return
        elif root.right is not None and root.left is None:
            # has rightchild
            root.right.value, root.value = root.value, root.right.value
            root.right = None
            self.length -= 1
            return

        # case 3: is a node with two child
        # change node with sucessor and remove sucessor until it turns a case 1 or case 2
        succ = self.successor(root)
        root.value = succ.value
        self.__delete_node(succ.value, succ)

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
