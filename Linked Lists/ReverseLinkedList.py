class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def create_linked_list(self, list_elements):
        self.head = ListNode(list_elements[0])

        i = 1
        current = self.head
        while i < len(list_elements):
            new_node = ListNode(list_elements[i])
            current.next = new_node
            current = new_node
            i = i + 1

    def reverse(self):
        if self.head is None or self.head.next is None:
            print("To reverse a linked list, it's length should be greater than 1.")
            return

        previous_node = None
        current_node = self.head
        next_node = current_node.next

        current_node.next = None

        while next_node is not None:
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next

            current_node.next = previous_node

        self.head = current_node

    def display(self):
        current = self.head
        while current.next is not None:
            print(f"{current.value}", end=' --> ')
            current = current.next
        print(f"{current.value}")


if __name__ == "__main__":
    linked_list_elements = input("Enter elements to create a linked list: ")
    linked_list_elements = list(linked_list_elements.split(' '))

    linked_list = LinkedList()
    linked_list.create_linked_list(linked_list_elements)

    print("\nElements of linked list before reversal are as follows:")
    linked_list.display()

    linked_list.reverse()
    print("\nElements of linked list after reversal are as follows:")
    linked_list.display()
