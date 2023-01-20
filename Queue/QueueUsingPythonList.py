class Queue:
    def __init__(self, max_length: int):
        self.queue = list()
        self.front = -1
        self.rear = -1
        self.MAX_LENGTH = max_length

    def isFull(self):
        if len(self.queue) == self.MAX_LENGTH:
            return True
        return False
    
    def isEmpty(self):
        if len(self.queue) == 0: 
            return True
        return False
    
    def enqueue(self, value):
        if self.isFull():
            print("Queue is full! Can't enqueue in a filled up queue.")
        elif self.isEmpty():
            self.front = 0
        self.queue.append(value)
        self.rear = self.rear + 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty! Can't dequeue from an empty queue.")
        elif (self.front == 0) and (self.rear == 0):
            self.queue = list()
            self.front = self.rear = -1
        else:
            self.queue.pop(0)
            self.rear = self.rear - 1

    def peek(self):
        if self.isEmpty():
            print("Queue is empty! Can't peek inside an empty queue.")
        else:
            print(self.queue[self.front])
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty! Can't display an empty queue.")
        else:
            print(self.queue)

if __name__ == "__main__":
    max_length = int(input("Input the maximum size of the queue: "))
    queue = Queue(max_length)

    while True:
        print()
        print("PROGRAM TO IMPLEMENT QUEUE USING PYTHON LIST")
        print("============================================")
        print("1) Enqueue node in Queue.")
        print("2) Dequeue node from Queue.")
        print("3) Peek element inside the Queue.")
        print("4) Display Queue.")
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
            print("Elements of Queue are as follows:")
            queue.display()
        elif choice == 'q' or choice == 'Q':
            print("User prompted to quit the program...")
            break
        else:
            print("Invalid Input!")
            print("Please enter a choice from above mentioned operations.")
