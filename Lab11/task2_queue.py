class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue:", queue.items)
    print("Front element:", queue.peek())
    print("Removed element:", queue.dequeue())
    print("Queue after dequeue:", queue.items)
    print("Queue size:", queue.size())
