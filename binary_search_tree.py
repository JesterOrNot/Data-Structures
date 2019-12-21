"""Binary Search Tree."""


class BinarySearchTreeNode:
    """Class For Binary Search Tree Node."""

    def __init__(self, value):
        """Construct Binary Search Tree Node."""
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    """Class for Binary Search Tree."""

    def __init__(self):
        """Construct Binary Search Tree."""
        super(BinarySearchTree, self).__init__()
        self.root = None

    @classmethod
    def print_preorder(cls, root):
        """Print binary search tree with preorder: root, left, right."""
        def printer():
            if not root:
                return

            print(root.value, end=" ")
            cls.print_preorder(root.left)
            cls.print_preorder(root.right)
        printer()
        print()

    @classmethod
    def print_inorder(cls, root):
        """Print binary search tree with inorder: left, root, right."""
        def printer():
            if not root:
                return

            cls.print_inorder(root.left)
            print(root.value, end=" ")
            cls.print_inorder(root.right)
        printer()
        print()

    @classmethod
    def print_postorder(cls, root):
        """Print binary search tree with postorder: left, right, root."""
        def printer():
            if not root:
                return
            cls.print_postorder(root.left)
            cls.print_postorder(root.right)
            print(root.value, end=" ")
        printer()
        print()

    @classmethod
    def print_outorder(cls, root):
        """Print binary search tree with outorder: right, root, left."""
        def printer():
            if not root:
                return
            cls.print_outorder(root.left)
            cls.print_outorder(root.right)
            print(root.value, end=" ")
        printer()
        print()

    @staticmethod
    def assemble_tree(the_list):
        """Assemble Binary Search Tree based on the given list."""
        #  WIP


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.root = BinarySearchTreeNode(5)
    tree.print_inorder(tree.root)
