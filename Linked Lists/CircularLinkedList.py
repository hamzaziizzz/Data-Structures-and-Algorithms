class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, index, value):
        new_node = ListNode(value)
        if self.head is None:
            print("Linked List is empty! Creating a new node as head.")
            self.head = new_node
            self.head.next = self.head
            return
        
        current = self.head
        if index == 0:
            while current.next is not self.head:
                current = current.next
            self.head = new_node
        else:
            i = 0
            while (current.next is not self.head) and (i != (index - 1)):
                current = current.next
                i += 1
        new_node.next = current.next
        current.next = new_node
    
    def search(self, value):
        if self.head is None:
            print("Linked List is empty! Can't search in an empty linked list.")
        else:
            current = self.head
            i = 0
            while (current.next is not self.head) and (current.value != value):
                current = current.next
                i += 1
            if (current.next is self.head) and (current.value != value):
                print(f"Value {value} is present in the list.")
            else:
                print(f"Value {value} is found at index {i}")
    
    def delete(self, value):
        if self.head is None:
            print("Linked List is empty! Can't delete from empty linked list.")
        elif self.head.next is self.head:
            self.head = None
        else:
            current = self.head
            while (current.next is not self.head) and (current.next.value != value):
                current = current.next
            if (current.next is self.head) and (current.next.value != value):
                print(f"Value {value} is not present in the list.")
            else:
                delete_node = current.next
                current.next = delete_node.next
                if delete_node is self.head:
                    self.head = delete_node.next
                delete_node.next = None
    
    def display(self):
        if self.head is None:
            print("Linked List is empty! Can't diplay/print an empty linked list.")
        else:
            current = self.head
            while current.next is not self.head:
                print(f"{current.value} --> ", end='')
                current = current.next
            print(f"{current.value}")


if __name__ == "__main__":
    choice = None
    circularLinkedList = CircularLinkedList()

    while choice != 'q':
        print()
        print("PR0GRAM TO IMPLEMENT CIRCULAR LINKED LIST")
        print("=========================================")
        print("1) Insert node")
        print("2) Delete node")
        print("3) Search node")
        print("4) Display Linked List")
        print("Type 'q' to quit.")
        print()

        choice = input("Enter your choice of operation: ")

        if choice == '1':
            value = input("Enter value for node: ")
            index = int(input("Enter index of insertion: "))
            circularLinkedList.insert(index, value)
        elif choice == '2':
            value = input("Enter value to be deleted: ")
            circularLinkedList.delete(value)
        elif choice == '3':
            value = input("Enter value to be searched: ")
            circularLinkedList.search(value)
        elif choice == '4':
            circularLinkedList.display()
        elif choice == 'q' or choice == 'Q':
            print("User prompted to quit the program...")
            break
        else:
            print("Invalid input!")
            print("Please enter a value from the above mentioned operations.")
