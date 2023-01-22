class TreeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None) -> None:
        self.root = root

    def insert_node(self, data) -> None:
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
        else:
            parent = None
            current = self.root
            while current is not None:
                parent = current
                if data < current.data:
                    current = current.left
                elif data > current.data:
                    current = current.right
            if data < parent.data:
                parent.left = new_node
            elif data > parent.data:
                parent.right = new_node

    @staticmethod
    def __inorder_successor(tree: TreeNode) -> TreeNode:
        maximum = tree.right
        while maximum.left is not None:
            maximum = maximum.left
        return maximum

    @staticmethod
    def __inorder_predecessor(tree: TreeNode) -> TreeNode:
        maximum = tree.left
        while maximum.right is not None:
            maximum = maximum.right
        return maximum

    def delete_node(self, data) -> None:
        if self.root is None:
            print("Tree is empty! Can't delete node from an empty tree.")
            return
        else:
            current = self.root
            parent = None
            while (current is not None) and (current.data != data):
                parent = current
                if data < current.data:
                    current = current.left
                elif data > current.data:
                    current = current.right
            if current is None:
                print(f"Node with data {data} is not present in binary search tree.")
                return
            else:
                if (current.left is None) and (current.right is None):
                    if parent is None:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    elif parent.right == current:
                        parent.right = None
                elif current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    elif parent.right == current:
                        parent.right = current.right
                elif current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    elif parent.right == current:
                        parent.right = current.left
                    del current
                elif (current.left is not None) and (current.right is not None):
                    inorder_predecessor = self.__inorder_predecessor(current)
                    self.delete_node(inorder_predecessor.data)
                    current.data = inorder_predecessor.data

    def __traverse_inorder(self, tree: TreeNode) -> None:
        if self.root is None:
            print("Tree is empty! Can't traverse an empty tree.")
            return
        if tree is not None:
            self.__traverse_inorder(tree.left)
            print(tree.data, end="  ")
            self.__traverse_inorder(tree.right)

    def inorder_traversal(self) -> None:
        tree = self.root
        self.__traverse_inorder(tree)

    def __traverse_preorder(self, tree: TreeNode) -> None:
        if self.root is None:
            print("Tree is empty! Can't traverse an empty tree.")
            return
        if tree is not None:
            print(tree.data, end="  ")
            self.__traverse_preorder(tree.left)
            self.__traverse_preorder(tree.right)

    def preorder_traversal(self) -> None:
        tree = self.root
        self.__traverse_preorder(tree)

    def __traverse_postorder(self, tree: TreeNode) -> None:
        if self.root is None:
            print("Tree is empty! Can't traverse an empty tree.")
            return
        if tree is not None:
            self.__traverse_postorder(tree.left)
            self.__traverse_postorder(tree.right)
            print(tree.data, end="  ")

    def postorder_traversal(self) -> None:
        tree = self.root
        self.__traverse_postorder(tree)

    def breadth_first_traversal(self):
        if self.root is None:
            print("Tree is empty! Can't traverse an empty tree.")
            return

        queue = [self.root]
        while len(queue) != 0:
            current = queue.pop(0)
            print(current.data, end="  ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    def depth_first_traversal(self, traversal: str) -> None:
        if self.root is None:
            print("Tree is empty! Can't traverse an empty tree.")
            return

        if traversal == 'inorder':
            stack = []
            current = self.root
            while True:
                if current is not None:
                    stack.insert(0, current)
                    current = current.left
                elif len(stack) != 0:
                    current = stack.pop(0)
                    print(current.data, end="  ")
                    current = current.right
                else:
                    break

        elif traversal == 'preorder':
            stack = [self.root]
            while len(stack) != 0:
                current = stack.pop(0)
                print(current.data, end="  ")
                if current.right is not None:
                    stack.insert(0, current.right)
                if current.left is not None:
                    stack.insert(0, current.left)

        elif traversal == 'postorder':
            stack = []
            current = self.root
            while True:
                while current is not None:
                    if current.right is not None:
                        stack.insert(0, current.right)
                    stack.insert(0, current)
                    current = current.left
                current = stack.pop(0)
                if current.right is not None and (len(stack) > 0 and stack[0] == current.right):
                    stack.pop(0)
                    stack.insert(0, current)
                    current = current.right
                else:
                    print(current.data, end="  ")
                    current = None
                if len(stack) == 0:
                    break


if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()

    while True:
        print()
        print("PROGRAM TO IMPLEMENT BINARY SEARCH TREE USING LINKED LIST")
        print("=========================================================")
        print("1) Insert Node")
        print("2) Delete Node")
        print("3) Inorder Traversal using Recursion")
        print("4) Preorder Traversal using Recursion")
        print("5) Postorder Traversal using Recursion")
        print("6) Breadth-first or Level Order Traversal")
        print("7) Depth-first Traversal ----")
        print("\t i)   Inorder Traversal")
        print("\t ii)  Preorder Traversal")
        print("\t iii) Postorder Traversal")
        print()
        print("Type 'q' to quit the program.")
        print()

        choice = input("Enter your choice of operation: ")
        print()

        if choice == '1':
            value = input("Enter value to be inserted in binary search tree: ")
            try:
                int(value)
                value = int(value)
            except ValueError:
                value = value
            binary_search_tree.insert_node(value)
            print(f"{value} is successfully inserted.")
        elif choice == '2':
            value = input("Enter value to be deleted from binary search tree: ")
            try:
                int(value)
                value = int(value)
            except ValueError:
                value = value
            binary_search_tree.delete_node(value)
            print(f"Node with data {value} is successfully deleted.")
        elif choice == '3':
            print("Inorder traversal of binary search tree is as follows:")
            binary_search_tree.inorder_traversal()
            print()
        elif choice == '4':
            print("Preorder traversal of binary search tree is as follows:")
            binary_search_tree.preorder_traversal()
            print()
        elif choice == '5':
            print("Postorder traversal of binary search tree is as follows:")
            binary_search_tree.postorder_traversal()
            print()
        elif choice == '6':
            print("Breadth-first traversal of binary search tree is as follows:")
            binary_search_tree.breadth_first_traversal()
            print()
        elif choice == '7':
            choose = input("Which depth-first traversal do you want to perform: ")
            if choose == 'i':
                print("Inorder traversal of binary search tree is as follows:")
                binary_search_tree.depth_first_traversal('inorder')
                print()
            elif choose == 'ii':
                print("Preorder traversal of binary search tree is as follows:")
                binary_search_tree.depth_first_traversal('preorder')
                print()
            elif choose == 'iii':
                print("Postorder traversal of binary search tree is as follows:")
                binary_search_tree.depth_first_traversal('postorder')
                print()
        elif choice == 'q' or choice == 'Q':
            print("USER PROMPTED TO QUIT THE PROGRAM...")
            break
        else:
            print("Invalid Input! Please enter your choice from the above mentioned operations only.")
