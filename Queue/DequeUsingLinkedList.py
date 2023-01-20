class QueueNode:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class DoublyEndedQueue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def isEmpty(self):
        if self.front is None:
            return True
        return False

    def insertFront(self, value):
        new_node = QueueNode(value)
        if self.front is None:
            self.front = new_node
            self.rear = self.front
        else:
            new_node.next = self.front
            self.front.previous = new_node
            self.front = new_node

    def insertRear(self, value):
        new_node = QueueNode(value)
        if self.front is None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            new_node.previous = self.rear
            self.rear = new_node

    def deleteFront(self):
        if self.isEmpty():
            print("Queue is empty! Can't delete from an empty queue.")
        else:
            delete_node = self.front
            self.front = self.front.next
            delete_node.next = None
            self.front.previous = None
            delete_node = None

    def deleteRear(self):
        if self.isEmpty():
            print("Queue is empty! Can't delete from an empty queue.")
        else:
            delete_node = self.rear
            self.rear = self.rear.previous
            delete_node.previous = None
            self.rear.next = None
            delete_node = None

    def getFront(self):
        if self.isEmpty():
            print("Queue is empty! Can't peek value from an empty queue.")
        else:
            print(f"The value of front node is {self.front.value}")

    def getRear(self):
        if self.isEmpty():
            print("Queue is empty! Can't peek value from an empty queue.")
        else:
            print(f"The value of rear node is {self.rear.value}")

    def displayForward(self):
        if self.isEmpty():
            print("Queue is empty! Can't display an empty queue.")
        else:
            current = self.front
            print("Elements of Doubly Ended Queue from front to rear are as follows:")
            while current is not self.rear:
                print(f"{current.value}", end=" --> ")
                current = current.next
            print(f"{current.value}")

    def displayBackward(self):
        if self.isEmpty():
            print("Queue is empty! Can't display an empty queue.")
        else:
            current = self.rear
            print("Elements of Doubly Ended Queue from rear to front are as follows:")
            while current is not self.front:
                print(f"{current.value}", end=" --> ")
                current = current.previous
            print(f"{current.value}")


if __name__ == "__main__":
    queue = DoublyEndedQueue()

    while True:
        print()
        print("PROGRAM TO IMPLEMENT DOUBLY ENDED QUEUE (DEQUE) USING DOUBLY LINKED LIST")
        print("========================================================================")
        print("1) Insert element at front of deque.")
        print("2) Insert element at rear of deque.")
        print("3) Delete element from front of deque.")
        print("4) Delete element from rear of deque.")
        print("5) Get element from front of deque.")
        print("6) Get element from rear of deque.")
        print("7) Display Queue in forward manner.")
        print("8) Display Queue in backward manner.")
        print("Type 'q' or 'Q' to quit the program!")
        print()

        choice = input("Enter your choice of operation: ")

        if choice == '1':
            value = input("Enter value to be inserted inside deque: ")
            queue.insertFront(value)
        elif choice == '2':
            value = input("Enter value to be inserted inside deque: ")
            queue.insertRear(value)
        elif choice == '3':
            queue.deleteFront()
        elif choice == '4':
            queue.deleteRear()
        elif choice == '5':
            queue.getFront()
        elif choice == '6':
            queue.getRear()
        elif choice == '7':
            queue.displayForward()
        elif choice == '8':
            queue.displayBackward()
        elif choice in "qQ":
            print("User prompted to quit the program...")
            break
        else:
            print("Invalid Input! Please enter choice only from above mentioned options.")
