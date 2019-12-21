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
    def print_preorder(cls, root) -> None:
        """Print binary search tree with preorder: root, left, right."""
        if not root:
            return

        print(root.value, end=" | ")
        cls.print_preorder(root.left)
        cls.print_preorder(root.right)

    @classmethod
    def print_inorder(cls, root) -> None:
        """Print binary search tree with inorder: left, root, right."""
        if not root:
            return

        cls.print_inorder(root.left)
        print(root.value, end=" | ")
        cls.print_inorder(root.right)

    @classmethod
    def print_postorder(cls, root) -> None:
        """Print binary search tree with postorder: left, right, root."""
        if not root:
            return
        cls.print_postorder(root.left)
        cls.print_postorder(root.right)
        print(root.value, end=" | ")

    @classmethod
    def print_outorder(cls, root) -> None:
        """Print binary search tree with outorder: right, root, left."""
        def printer():
            if not root:
                return
            cls.print_outorder(root.left)
            cls.print_outorder(root.right)
            print(root.value, end=" | ")
        printer()
        print()

    @classmethod
    def insert_node(cls, node, root) -> BinarySearchTreeNode:
        if root is None:
            return node
        if node.value < root.value:
            root.left = cls.insert_node(node, root.left)
        else:
            root.right = cls.insert_node(node, root.right)
        return root

    @staticmethod
    def assemble_tree(node_list) -> BinarySearchTree:
        """Assemble Binary Search Tree based on the given list."""
        tree = BinarySearchTree()
        tree.root = BinarySearchTreeNode(node_list[0])
        index = 1
        while index <= len(node_list)-1:
            tree.insert_node(BinarySearchTreeNode(node_list[index]), tree.root)
            index += 1
        return tree

    @classmethod
    def find_node(cls, target, tree, current) -> bool:
        if target == current.value:
            return True
        elif target < current.value:
            if current.left is not None:
                current = current.left
            else:
                return False
        elif target >= current.value:
            if current.right is not None:
                current = current.right
            else:
                return False
        return cls.find_node(target, tree, current)


if __name__ == "__main__":
    TREE = BinarySearchTree.assemble_tree([5, 2, 1, 0, 3.10, 3.5, -3])
    print("| ", end="")
    TREE.print_inorder(TREE.root)
    print()
    print(TREE.find_node(-6, TREE, TREE.root))
