class CircularQueue:
    def __init__(self, max_length):
        self.front = -1
        self.rear = -1
        self.MAX_LENGTH = max_length
        self.queue = [None] * self.MAX_LENGTH

    def isFull(self):
        if ((self.rear + 1) % self.MAX_LENGTH) == self.front:
            return True
        return False

    def isEmpty(self):
        if self.front == -1:
            return True
        return False

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full! Can't enqueue is a filled up queue.")
        elif self.isEmpty():
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.MAX_LENGTH
            self.queue[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty! Can't dequeue element from an empty queue.")
        else:
            self.queue[self.front] = None
            if (self.front == self.rear) and (self.front != -1):
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.MAX_LENGTH

    def peek(self):
        if self.isEmpty():
            print("Queue is empty! Can't peek element from an empty queue.")
        else:
            print(f"Front element of circular queue is {self.queue[self.front]}")

    def display(self):
        if self.isEmpty():
            print("Queue is empty! Can't display an empty queue.")
        else:
            print("Elements of circular queue are as follows:")
            if self.front == self.rear:
                print(f"{self.queue[self.front]}")
            elif self.front < self.rear:
                for i in range(self.front, self.rear):
                    print(f"{self.queue[i]}", end=" --> ")
                print(f"{self.queue[self.rear]}")
            elif self.front > self.rear:
                i = self.front
                while i < self.MAX_LENGTH:
                    print(f"{self.queue[i]}", end=" --> ")
                    i = i + 1
                j = i % self.MAX_LENGTH
                while j < (self.rear):
                    print(f"{self.queue[j]}", end=" --> ")
                    j = j + 1
                print(f"{self.queue[self.rear]}")


if __name__ == "__main__":
    max_length = int(input("Input the maximum size of Circular Queue: "))
    queue = CircularQueue(max_length)

    while True:
        print()
        print("PROGRAM TO IMPLEMENT CIRCULAR QUEUE USING PYTHON LIST")
        print("=====================================================")
        print("1) Enqueue node in Circular Queue.")
        print("2) Dequeue node from Cirular Queue.")
        print("3) Peek element inside the Circular Queue.")
        print("4) Display Circular Queue.")
        print("Type 'q' to quit.")
        print()

        choice = input("Enter your choice of operartion: ")

        if choice == '1':
            value = input("Enter value to be enqueued inside the queue: ")
            queue.enqueue(value)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.peek()
        elif choice == '4':
            queue.display()
        elif choice == 'q' or choice == 'Q':
            print("User prompted to quit the program...")
        else:
            print("Invalid Input!")
            print("Please enter a choice from above mentioned operations.")
