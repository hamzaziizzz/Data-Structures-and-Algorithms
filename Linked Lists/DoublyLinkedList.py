class ListNode:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, index, value):
        if self.head is None:
            print("Linked List is empty! Inserting head node.")
            self.head = ListNode(value)
        elif index == 0:
            current = self.head
            new_node = ListNode(value)
            new_node.next = current
            current.previous = new_node
            self.head = new_node
        else:
            new_node = ListNode(value)
            i = 0
            current = self.head
            while current is not None and i != (index - 1):
                current = current.next
                i += 1
            if current is None:
                print("Invalid index!")
            else:
                new_node.next = current.next
                current.next = new_node
                new_node.previous = current
                if new_node.next is not None:
                    new_node.next.previous = new_node

    def delete(self, value):
        if self.head is None:
            print("Linked List is empty! Cannot delete node from an empty linked list.")
        elif self.head.next is None:
            print("Linked List contains single node. Deleting it would result in an empty linked list.")
            decision = input("Enter 'y' to confirm otherwise 'n' to cancel: ")
            if decision == 'y':
                self.head = None
        else:
            current = self.head
            if current.value == value:
                self.head = self.head.next
                current.next = None
                self.head.previous = None
            else:
                while current.next is not None and current.next.value != value:
                    current = current.next
                if current.next is None:
                    print(f"Linked List does not contain any node of value {value}")
                else:
                    delete_node = current.next
                    current.next = delete_node.next
                    delete_node.previous = current
                    delete_node.next = None
                    delete_node.previous = None

    def search(self, value):
        if self.head is None:
            print("Linked List is empty! Cannot search into an empty linked list.")
        elif self.head.value == value:
            print(f"Value {value} is found at index 0")
        else:
            current = self.head
            i = 0
            while current is not None and current.value != value:
                current = current.next
                i += 1
            if current is None:
                print(f"Linked List does not contain any node of value {value}")
            else:
                print(f"Value {value} is found at index {i}")

    def display_forward(self):
        if self.head is None:
            print("Linked List is empty! Cannot display an empty linked list.")
        else:
            print("Elements of Linked List are as follows:")
            current = self.head
            while current.next is not None:
                print(f"{current.value} --> ", end='')
                current = current.next
            print(f"{current.value}")

    def display_backward(self):
        if self.head is None:
            print("Linked List is empty! Cannot display an empty linked list.")
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            print("Elements of Linked List are as follows:")
            while current.previous is not None:
                print(f"{current.value} --> ", end='')
                current = current.previous
            print(f"{current.value}")


if __name__ == "__main__":
    choice = -1
    doublyLinkedList = DoublyLinkedList()

    while choice != 'q':
        print()
        print("PR0GRAM TO IMPLEMENT DOUBLY LINKED LIST")
        print("=======================================")
        print("1) Insert node")
        print("2) Delete node")
        print("3) Search node")
        print("4) Display Linked List in Forward Manner")
        print("5) Display Linked List in Backward Manner")
        print("Type 'q' to quit.")
        print()

        choice = input("Enter your choice of operation: ")

        if choice == '1':
            value = input("Enter value for node: ")
            index = int(input("Enter index of insertion: "))
            doublyLinkedList.insert(index, value)
        elif choice == '2':
            value = input("Enter value to be deleted: ")
            doublyLinkedList.delete(value)
        elif choice == '3':
            value = input("Enter value to be searched: ")
            doublyLinkedList.search(value)
        elif choice == '4':
            doublyLinkedList.display_forward()
        elif choice == '5':
            doublyLinkedList.display_backward()
        elif choice == 'q' or choice == 'Q':
            print("User prompted to quit the program...")
            break
        else:
            print("Invalid input!")
            print("Please enter a value from the above mentioned operations.")
