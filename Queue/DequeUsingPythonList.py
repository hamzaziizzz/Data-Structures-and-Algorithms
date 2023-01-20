class DoublyEndedQueue:
    def __init__(self, max_length):
        self.queue = list()
        self.front = 0
        self.rear = len(self.queue) - 1
        self.MAX_LENGTH = max_length

    def isFull(self):
        if len(self.queue) == self.MAX_LENGTH:
            return True
        return False

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    def insertFront(self, value):
        if self.isFull():
            print("Queue is full! Can't insert element in a filled up queue.")
        else:
            self.queue.insert(0, value)
        self.rear = len(self.queue) - 1

    def insertRear(self, value):
        if self.isFull():
            print("Queue is full! Can't insert element in a filled up queue.")
        else:
            self.queue.append(value)
        self.rear = len(self.queue) - 1

    def deleteFront(self):
        if self.isEmpty():
            print("Queue is empty! Can't delete element from an empty queue.")
        else:
            self.queue.pop(0)
        self.rear = len(self.queue) - 1

    def deleteRear(self):
        if self.isEmpty():
            print("Queue is empty! Can't delete element from an empty queue.")
        else:
            self.queue.pop()
        self.rear = len(self.queue) - 1

    def getFront(self):
        if self.isEmpty():
            print("Queue is empty! Can't peek element from an empty queue.")
        else:
            print(f"Front element of doubly ended is {self.queue[self.front]}")

    def getRear(self):
        if self.isEmpty():
            print("Queue is empty! Can't peek element from an empty queue.")
        else:
            print(f"Rear element of doubly ended is {self.queue[self.rear]}")

    def displayForward(self):
        if self.isEmpty():
            print("Queue is empty! Can't display an empty queue.")
        else:
            print("Elements of Doubly Ended Queue from front to rear are as follows:")
            for i in range(self.front, self.rear):
                print(f"{self.queue[i]}", end = " --> ")
            print(f"{self.queue[self.rear]}")

    def displayBackward(self):
        if self.isEmpty():
            print("Queue is empty! Can't display an empty queue.")
        else:
            print("Elements of Doubly Ended Queue from rear to front are as follows:")
            for i in range(self.rear, self.front, -1):
                print(f"{self.queue[i]}", end=" --> ")
            print(f"{self.queue[self.front]}")


if __name__ == "__main__":
    max_length = int(input("Input the maximum size of the queue: "))
    queue = DoublyEndedQueue(max_length)

    while True:
        print()
        print("PROGRAM TO IMPLEMENT DOUBLY ENDED QUEUE (DEQUE) USING PYTHON LIST")
        print("=================================================================")
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
