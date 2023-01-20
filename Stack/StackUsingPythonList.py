class Stack:
    def __init__(self, max_length: int) -> None:
        self.__MAX_SIZE = max_length
        self.__top = -1
        self.__stack = [None] * max_length

    def get_top(self):
        return self.__top

    def is_full(self) -> bool:
        if self.__top == (self.__MAX_SIZE - 1):
            return True
        return False

    def is_empty(self) -> bool:
        if self.__top == (-1):
            return True
        return False

    def size(self) -> int:
        return self.__top + 1

    def push(self, key):
        if self.is_full():
            print("Stack is full! Can't push element into a filled up stack.")
            return
        self.__top = self.__top + 1
        self.__stack[self.__top] = key

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Can't pop element from an empty stack.")
            return
        self.__stack[self.__top] = None
        self.__top = self.__top - 1

    def peek(self):
        if self.is_empty():
            print("Stack is empty! Can't peek element from an empty stack.")
            return
        return self.__stack[self.__top]

    def display(self):
        if self.is_empty():
            print("Stack is empty! Can't display an empty stack.")
            return
        return self.__stack[(self.__top+1)::(-1)]


if __name__ == "__main__":
    max_size = int(input("Enter maximum size for the stack_data_structure to be implemented: "))
    stack_data_structure = Stack(max_size)

    while True:
        print()
        print("PROGRAM TOP IMPLEMENT STACK USING LINKED LIST")
        print("=============================================")
        print("1) Push element into the stack.")
        print("2) Pop element out of the stack.")
        print("3) Peek top element of stack.")
        print("4) Print current size of stack.")
        print("5) Check if stack is full.")
        print("6) Check if stack is empty.")
        print("7) Display elements of stack.")
        print("Type 'q' or 'Q' to quit the program.")
        print()

        choice = input("Enter your choice of operation: ")

        if choice == '1':
            value = input("Enter value to be pushed inside the stack: ")
            stack_data_structure.push(value)
        elif choice == '2':
            print(f"{stack_data_structure.peek()} is popped out of stack.")
            stack_data_structure.pop()
        elif choice == '3':
            print(f"Top element of stack is {stack_data_structure.peek()}")
        elif choice == '4':
            print(f"Current size of stack is {stack_data_structure.size()}")
        elif choice == '5':
            if stack_data_structure.is_full():
                print("Stack has been filled up to its maximum size.")
            else:
                print(f"Stack still has capacity of {(max_size - 1) - stack_data_structure.get_top()} elements.")
        elif choice == '6':
            if stack_data_structure.is_empty():
                print(f"Stack is empty! There is no element present inside stack and has capacity of "
                      f"{max_size} elements.")
            else:
                print(f"There are {stack_data_structure.get_top() + 1} elements present in stack.")
        elif choice == '7':
            print("Elements of stack are as follows:")
            print(stack_data_structure.display())
        elif choice in "qQ":
            print("User prompted to quit the program...")
            break
        else:
            print("Invalid input! Please enter your choice only from above mentioned options.")
