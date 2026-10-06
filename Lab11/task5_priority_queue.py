import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (-priority, item))

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        priority, item = heapq.heappop(self.queue)
        return item

    def display(self):
        print("Priority Queue:", self.queue)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Normal Task", 1)
    pq.enqueue("Important Task", 3)
    pq.enqueue("Urgent Task", 5)

    pq.display()
    print("Removed:", pq.dequeue())
    print("Removed:", pq.dequeue())
    print("Removed:", pq.dequeue())
