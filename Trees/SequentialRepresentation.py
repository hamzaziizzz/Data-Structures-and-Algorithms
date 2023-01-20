class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def sequential_representation(self, tree: list):
        self.root = tree

    def left_child(self, node):
        if node not in self.root:
            print(f"Node {node} is not present in binary tree.")
            return

        index = self.root.index(node)
        left_child_index = (2 * index) + 1
        if left_child_index > (len(self.root) - 1):
            print(f"Node {node} is a leaf node.")
            return

        if self.root[left_child_index] is None:
            print(f"Node {node} does not have a left child.")
            return

        return self.root[left_child_index], left_child_index

    def right_child(self, node):
        if node not in self.root:
            print(f"Node {node} is not present in binary tree.")
            return

        index = self.root.index(node)
        right_child_index = (2 * index) + 2
        if right_child_index > (len(self.root) - 1):
            print(f"Node {node} is a leaf node.")
            return

        if self.root[right_child_index] is None:
            print(f"Node {node} does not have a right child.")
            return

        return self.root[right_child_index], right_child_index

    def parent(self, node):
        if node not in self.root:
            print(f"Node {node} is not present in binary tree.")
            return

        index = self.root.index(node)
        parent_index = (index - 1) // 2
        if parent_index < 0:
            print(f"Node {node} is the root node.")
            return

        return self.root[parent_index], parent_index

    def display(self):
        return self.root


if __name__ == "__main__":
    binary_tree = BinaryTree()

    binary_tree_list = input("Enter the value of nodes (seperated by a comma) to be inserted in a binary tree:\n")
    binary_tree_list = list(binary_tree_list.split(', '))
    for i, tree_node in enumerate(binary_tree_list):
        if tree_node == 'null':
            binary_tree_list[i] = None

    binary_tree.sequential_representation(binary_tree_list)

    while True:
        print()
        print("PROGRAM TO REPRESENT A BINARY TREE USING PYTHON LIST")
        print("====================================================")
        print("1) Display sequential representation of binary tree.")
        print("2) Find left child of a given node.")
        print("3) Find right child of a given node.")
        print("Type 'q' to quit the program.")
        print()

        choice = input("Enter your choice of operation: ")
        print()

        if choice == '1':
            print("Sequential representation of binary tree is as follows:")
            print(binary_tree.display())
        elif choice == '2':
            binary_tree_node = input("Which node's left child do you want to find out? ")
            left_child = binary_tree.left_child(binary_tree_node)
            if left_child is not None:
                print(f"Left child of node {binary_tree_node} is node {left_child[0]} and is present at index {left_child[1]}")
        elif choice == '3':
            binary_tree_node = input("Which node's right child do you want to find out? ")
            right_child = binary_tree.right_child(binary_tree_node)
            if right_child is not None:
                print(f"Right child of node {binary_tree_node} is node {right_child[0]} and is present at index {right_child[1]}")
        elif choice == '4':
            binary_tree_node = input("Which node's parent do you want to find out? ")
            parent = binary_tree.parent(binary_tree_node)
            if parent is not None:
                print(f"Parent of node {binary_tree_node} is node {parent[0]} and is present at index {parent[1]}")
        elif choice in 'qQ':
            print("USER PROMPTED TO QUIT THE PROGRAM...")
            break
        else:
            print("Invalid Input! Please enter your choice from the above mentioned operations only.")
