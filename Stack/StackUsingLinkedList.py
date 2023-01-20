class StackNode:
    def __init__(self, element):
        self.__value = element
        self.__bottom = None

    def get_value(self):
        return self.__value

    def get_bottom(self):
        return self.__bottom

    def set_bottom(self, bottom):
        self.__bottom = bottom


class Stack:
    def __init__(self):
        self.__top = None

    def isEmpty(self):
        if self.__top is None:
            return True
        return False

    def push(self, element):
        new_node = StackNode(element)
        if self.__top is None:
            self.__top = new_node
        else:
            new_node.set_bottom(self.__top)
            self.__top = new_node

    def pop(self):
        if self.__top is None:
            print("Stack is empty! Can't pop element from an empty stack.")
        else:
            pop_node = self.__top
            self.__top = self.__top.get_bottom()
            pop_node.set_bottom(None)

    def peek(self):
        if self.__top is None:
            print("Stack is empty! Can't peek element from an empty stack.")
        else:
            print(f"Top element of stack is {self.__top.get_value()}")

    def size(self):
        i = 0
        current = self.__top
        while current is not None:
            current = current.get_bottom()
            i = i + 1
        print(f"Current size of stack_data_structure is {i}")

    def display(self):
        if self.__top is None:
            print("Stack is empty! Can't display an empty stack.")
        else:
            current = self.__top
            print("Elements of Stack are as follows:")
            while current.get_bottom() is not None:
                print(f"{current.get_value()}", end=" --> ")
                current = current.get_bottom()
            print(f"{current.get_value()}")


if __name__ == "__main__":
    stack = Stack()

    while True:
        print()
        print("PROGRAM TOP IMPLEMENT STACK USING LINKED LIST")
        print("=============================================")
        print("1) Push element into the stack.")
        print("2) Pop element out of the stack.")
        print("3) Peek top element of stack.")
        print("4) Print current size of stack.")
        print("5) Display elements of stack.")
        print("Type 'q' or 'Q' to quit the program.")
        print()

        choice = input("Enter your choice of operation: ")

        if choice == '1':
            value = input("Enter value to be pushed inside the stack: ")
            stack.push(value)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.size()
        elif choice == '5':
            stack.display()
        elif choice in "qQ":
            print("User prompted to quit the program...")
            break
        else:
            print("Invalid input! Please enter your choice only from above mentioned options.")