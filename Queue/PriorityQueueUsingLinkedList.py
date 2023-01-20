class QueueNode:
    def __init__(self, value, priority: int, next=None):
        self.value = value
        self.priority = priority
        self.next = next
    

class PriorityQueue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
    
    def enqueue(self, value, priority: int):
        new_node = QueueNode(value, priority)
        if self.front is None:
            self.front = new_node
            self.rear = self.front
        elif self.front.priority > priority:
            new_node.next = self.front
            self.front = new_node
        elif (self.rear.priority <= priority):
            self.rear.next = new_node
            self.rear = new_node
        else:
            current = self.front
            previous = None
            while current.priority <= priority:
                previous = current
                current = current.next
            previous.next = new_node
            new_node.next = current
    
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
    priorityQueue = PriorityQueue()

    choice = None

    while True:
        print()
        print("PROGRAM TO IMPLEMENT PRIORITY QUEUE USING LINKED LIST")
        print("=====================================================")
        print("1) Enqueue node in Queue.")
        print("2) Dequeue node from Queue.")
        print("3) Peek element inside the Queue.")
        print("4) Display Queue.")
        print("Type 'q' to quit.")
        print()

        choice = input("Enter your choice of operartion: ")

        if choice == '1':
            value = input("Enter value to be enqueued inside the queue: ")
            priority = int(input("Enter priority of the queue's element to be enqueued: "))
            priorityQueue.enqueue(value, priority)
        elif choice == '2':
            priorityQueue.dequeue()
        elif choice == '3':
            priorityQueue.peek()
        elif choice == '4':
            print("Elements of Queue are as follows:")
            priorityQueue.display()
        elif choice == 'q' or choice == 'Q':
            print("User prompted to quit the program...")
            break
        else:
            print("Invalid Input!")
            print("Please enter a choice from above mentioned operations.")
