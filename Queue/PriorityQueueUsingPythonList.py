class PriorityQueueElement:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self, max_length):
        self.priority_queue = list()
        self.front = -1
        self.rear = -1
        self.MAX_LENGTH = max_length

    def isFull(self):
        if len(self.priority_queue) == self.MAX_LENGTH:
            return True
        return False

    def isEmpty(self):
        if len(self.priority_queue) == 0:
            return True
        return False

    def enqueue(self, value, priority):
        new_element = PriorityQueueElement(value, priority)
        if self.isFull():
            print("Queue is full! Can't enqueue in a filled up queue.")
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.priority_queue.append(new_element)
        else:
            if priority < self.priority_queue[self.front].priority:
                self.priority_queue.insert(0, new_element)
            elif priority >= self.priority_queue[self.rear].priority:
                self.priority_queue.append(new_element)
            else:
                for i, current_element in enumerate(self.priority_queue):
                    if current_element.priority > priority:
                        break
                self.priority_queue.insert(i, new_element)
        
        self.rear = len(self.priority_queue) - 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty! Can't dequeue from an empty queue.")
        elif (self.front == 0) and (self.rear == 0):
            self.priority_queue = list()
            self.front = self.rear = -1
        else:
            self.priority_queue.pop(0)
            self.rear = self.rear - 1

    def peek(self):
        if self.isEmpty():
            print("Queue is empty! Can't peek inside an empty queue.")
        else:
            print(self.priority_queue[self.front].value)

    def display(self):
        if self.isEmpty():
            print("Queue is empty! Can't display an empty queue.")
        else:
            print("Elements of priority queue are as follows:")
            for current_element in self.priority_queue:
                print((current_element.value, current_element.priority), end='\t')
            print()


if __name__ == "__main__":
    max_length = int(input("Input the maximum size of the queue: "))
    priorityQueue = PriorityQueue(max_length)

    choice = None

    while True:
        print()
        print("PROGRAM TO IMPLEMENT PRIORITY QUEUE USING PYTHON LIST")
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
