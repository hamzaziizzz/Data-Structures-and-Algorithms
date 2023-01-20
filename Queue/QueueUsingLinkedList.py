class QueueNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
    
    def enqueue(self, value):
        new_node = QueueNode(value)
        if self.front is None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            print("Queue is empty! Can't dequeue from an empty queue.")
        elif self.front == self.rear:
            self.front = self.rear = None
        else:
            dequeue_node = self.front
            self.front = self.front.next
            dequeue_node.next = None
            dequeue_node = None
    
    def peek(self):
        if self.front is None:
            print("Queue is empty! Can't peek element inside an empty queue!")
        else:
            print(f"Front element of queue is {self.front.value}")
    
    def display(self):
        if self.front is None:
            print("Queue is empty! Can't display an empty queue.")
        else:
            current = self.front
            while current is not self.rear:
                print(f"{current.value} --> ", end='')
                current = current.next
            print(f"{current.value}")


if __name__ == "__main__":
    queue = Queue()

    choice = None

    while choice != 'q' or choice != 'Q':
        print()
        print("PROGRAM TO IMPLEMENT QUEUE USING LINKED LIST")
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
        else:
            print("Invalid Input!")
            print("Please enter a choice from above mentioned operations.")
