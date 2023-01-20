class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def construct_binary_tree(self, postorder=None,  preorder=None, inorder=None):
        if postorder is None:
            if (len(preorder) == 0) and (len(inorder) == 0):
                return

            subtree_root_node = TreeNode(preorder[0])
            index = inorder.index(preorder[0])

            inorder_left = inorder[:index]
            inorder_right = inorder[(index + 1):]

            preorder_left = preorder[1:(index + 1)]
            preorder_right = preorder[(index + 1):]

            subtree_root_node.left = self.construct_binary_tree(preorder=preorder_left, inorder=inorder_left)
            subtree_root_node.right = self.construct_binary_tree(preorder=preorder_right, inorder=inorder_right)

            return subtree_root_node

        elif preorder is None:
            if (len(postorder) == 0) and (len(inorder) == 0):
                return

            subtree_root_node = TreeNode(postorder[-1])
            index = inorder.index(postorder[-1])

            inorder_left = inorder[:index]
            inorder_right = inorder[(index + 1):]

            postorder_left = postorder[:index]
            postorder_right = postorder[index:(len(postorder) - 1)]

            subtree_root_node.left = self.construct_binary_tree(postorder=postorder_left, inorder=inorder_left)
            subtree_root_node.right = self.construct_binary_tree(postorder=postorder_right, inorder=inorder_right)

            return subtree_root_node

        elif inorder is None:
            if (len(preorder) == 0) and (len(postorder) == 0):
                return

            if (len(preorder) == 1) and (len(postorder) == 1):
                return TreeNode(preorder[0])

            subtree_root_node = TreeNode(preorder[0])
            left_child_index = postorder.index(preorder[1])

            postorder_left = postorder[:(left_child_index + 1)]
            postorder_right = postorder[(left_child_index + 1):(len(postorder) - 1)]

            preorder_left = preorder[1:(len(postorder_left) + 1)]
            preorder_right = preorder[(len(postorder_left) + 1):]

            subtree_root_node.left = self.construct_binary_tree(postorder=postorder_left, preorder=preorder_left)
            subtree_root_node.right = self.construct_binary_tree(postorder=postorder_right, preorder=preorder_right)

            return subtree_root_node

    def __traverse_postorder(self, tree: TreeNode):
        if tree is not None:
            self.__traverse_postorder(tree.left)
            self.__traverse_postorder(tree.right)
            print(tree.data, end="  ")

    def postorder_traversal(self):
        self.__traverse_postorder(self.root)

    def __traverse_preorder(self, tree: TreeNode):
        if tree is not None:
            print(tree.data, end="  ")
            self.__traverse_preorder(tree.left)
            self.__traverse_preorder(tree.right)

    def preorder_traversal(self):
        self.__traverse_preorder(self.root)

    def __traverse_inorder(self, tree: TreeNode):
        if tree is not None:
            self.__traverse_inorder(tree.left)
            print(tree.data, end="  ")
            self.__traverse_inorder(tree.right)

    def inorder_traversal(self):
        self.__traverse_inorder(self.root)


if __name__ == "__main__":
    binary_tree = BinaryTree()

    while True:
        print()
        print("PROGRAM TO CONSTRUCT A BINARY TREE FROM ITS TRAVERSAL")
        print("=====================================================")
        print("1) Construct Binary Tree from Preorder and Inorder Traversal")
        print("2) Construct Binary Tree from Postorder and Inorder Traversal")
        print("3) Construct Binary Tree from Preorder and Postorder Traversal")
        print("Type 'q' to quit the program.")
        print()

        choice = input("Enter your choice of operation: ")

        if choice == '1':
            preorder_traversal = input("\nEnter preorder traversal of binary tree (seperated by a comma):\n")
            preorder_traversal = list(preorder_traversal.split(', '))

            inorder_traversal = input("\nEnter inorder traversal of binary tree (seperated by a comma):\n")
            inorder_traversal = list(inorder_traversal.split(', '))

            binary_tree.root = binary_tree.construct_binary_tree(preorder=preorder_traversal, inorder=inorder_traversal)

            print("\nPostorder traversal of binary tree is as follows:")
            binary_tree.postorder_traversal()
            print()

        elif choice == '2':
            postorder_traversal = input("\nEnter postorder traversal of binary tree (seperated by a comma):\n")
            postorder_traversal = list(postorder_traversal.split(', '))

            inorder_traversal = input("\nEnter inorder traversal of binary tree (seperated by a comma):\n")
            inorder_traversal = list(inorder_traversal.split(', '))

            binary_tree.root = binary_tree.construct_binary_tree(postorder=postorder_traversal, inorder=inorder_traversal)

            print("\nPreorder traversal of binary tree is as follows:")
            binary_tree.preorder_traversal()
            print()

        elif choice == '3':
            postorder_traversal = input("\nEnter postorder traversal of binary tree (seperated by a comma):\n")
            postorder_traversal = list(postorder_traversal.split(', '))

            preorder_traversal = input("\nEnter preorder traversal of binary tree (seperated by a comma):\n")
            preorder_traversal = list(preorder_traversal.split(', '))

            binary_tree.root = binary_tree.construct_binary_tree(postorder=postorder_traversal, preorder=preorder_traversal)

            print("\nInorder traversal of binary tree is as follows:")
            binary_tree.inorder_traversal()
            print()

        elif choice == 'q' or choice == 'Q':
            print("USER PROMPTED TO QUIT THE PROGRAM...")
            break

        else:
            print("Invalid Input! Please enter your choice from the above mentioned operations only.")
