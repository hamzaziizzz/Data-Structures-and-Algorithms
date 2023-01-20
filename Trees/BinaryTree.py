class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = self.__create_binary_tree()

    def __create_binary_tree(self):
        value = input("Enter value to be inserted in binary tree: ")
        new_node = TreeNode(value)

        left_choice = input(f"\nDo you want to create left child for node {value} (y/n): ")
        if left_choice in "yY":
            new_node.left = self.__create_binary_tree()

        right_choice = input(f"\nDo you want to create right child for node {value} (y/n): ")
        if right_choice in "yY":
            new_node.right = self.__create_binary_tree()

        return new_node

    def __traverse_inorder(self, tree):
        if tree is not None:
            self.__traverse_inorder(tree.left)
            print(tree.data, end="  ")
            self.__traverse_inorder(tree.right)

    def inorder_traversal(self):
        tree = self.root
        self.__traverse_inorder(tree)

    def __traverse_preorder(self, tree):
        if tree is not None:
            print(tree.data, end="  ")
            self.__traverse_preorder(tree.left)
            self.__traverse_preorder(tree.right)

    def preorder_traversal(self):
        tree = self.root
        self.__traverse_preorder(tree)

    def __traverse_postorder(self, tree):
        if tree is not None:
            self.__traverse_postorder(tree.left)
            self.__traverse_postorder(tree.right)
            print(tree.data, end="  ")

    def postorder_traversal(self):
        tree = self.root
        self.__traverse_postorder(tree)


if __name__ == "__main__":
    binary_tree = None

    choice = None
    while True:
        print()
        print("PROGRAM TO IMPLEMENT BINARY TREE USING LINKED LIST")
        print("==================================================")
        print("1) Create Binary Tree")
        print("2) Inorder Traversal")
        print("3) Preorder Traversal")
        print("4) Postorder Traversal")
        print("Type 'q' to quit the program")
        print()

        choice = input("Enter your choice of operation: ")
        print()

        if choice == '1':
            binary_tree = BinaryTree()
        elif choice == '2':
            print("Inorder Traversal of Binary Tree is as follows:")
            binary_tree.inorder_traversal()
            print()
        elif choice == '3':
            print("Preorder Traversal of Binary Tree is as follows:")
            binary_tree.preorder_traversal()
            print()
        elif choice == '4':
            print("Postorder Traversal of Binary Tree is as follows:")
            binary_tree.postorder_traversal()
            print()
        elif choice == 'q' or choice == 'Q':
            print("User prompted to quit the program...")
            break
        else:
            print("Invalid Input! Please enter your choice from the above mentioned operations only.")
