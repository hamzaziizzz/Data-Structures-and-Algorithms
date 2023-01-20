class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, index, value):
        if self.head is None:
            self.head = ListNode(value)
        elif index == 0:
            current = self.head
            new_node = ListNode(value)
            new_node.next = current
            self.head = new_node
        else:
            new_node = ListNode(value)
            i = 0
            current = self.head
            while i != (index - 1) and current is not None:
                current = current.next
                i += 1
            if current is None:
                return "Invalid index!"
            new_node.next = current.next
            current.next = new_node

    def append(self, value):
        if self.head is None:
            self.head = ListNode(value)
        else:
            current = self.head
            new_node = ListNode(value)
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if self.head is None:
            print("Linked List is empty! Cannot delete node from an empty linked list.")
        elif self.head.next is None:
            print("Linked List contains single node. Deleting it would result in an empty linked list.")
            self.head = None
        else:
            current = self.head
            if current.value == value:
                self.head = self.head.next
                current.next = None
            else:
                while current.next is not None and current.next.value != value:
                    current = current.next
                if current.next is None:
                    print(f"Linked List does not contain any node of value {value}")
                else:
                    delete_node = current.next
                    current.next = delete_node.next
                    delete_node.next = None

    def search(self, value):
        if self.head.value == value:
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
    
    def length(self):
        if self.head is None:
            print("Linked List is empty! Length of linked list is 0")
        else:
            i = 0
            current = self.head
            while current is not None:
                current = current.next
                i = i + 1
            
            print(f"Length of linked list is {i}")

    def display(self):
        if self.head is None:
            print("Linked List is empty! Cannot display an empty linked list.")
        else:
            print("Elements of Linked List are as follows:")
            current = self.head
            while current.next is not None:
                print(f"{current.value} --> ", end='')
                current = current.next
            print(f"{current.value}")


if __name__ == "__main__":
    choice = None
    linkedList = LinkedList()

    while choice != 'q':
        print()
        print("PR0GRAM TO IMPLEMENT LINKED LIST")
        print("================================")
        print("1) Insert node")
        print("2) Append node")
        print("3) Delete node")
        print("4) Display length of Linked List")
        print("5) Display Linked List")
        print("6) Search node")
        print("Type 'q' to quit.")
        print()

        choice = input("Enter your choice of operation: ")

        if choice == '1':
            value = input("Enter value for node: ")
            index = int(input("Enter index of insertion: "))
            linkedList.insert(index, value)
        elif choice == '2':
            value = input("Enter value for node: ")
            linkedList.append(value)
        elif choice == '3':
            value = input("Enter value to be deleted: ")
            linkedList.delete(value)
        elif choice == '4':
            linkedList.length()
        elif choice == '5':
            linkedList.display()
        elif choice == '6':
            value = input("Enter value to be searched: ")
            linkedList.search(value)
        elif choice == 'q' or choice == 'Q':
            print("User prompted to quit the program...")
            break
        else:
            print("Invalid input!")
            print("Please enter a value from the above mentioned operations.")
