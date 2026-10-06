from collections import deque

class DequeDS:
    def __init__(self):
        self.items = deque()

    def insert_front(self, item):
        self.items.appendleft(item)

    def insert_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if len(self.items) == 0:
            return None
        return self.items.popleft()

    def remove_rear(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def display(self):
        print("Deque:", list(self.items))


if __name__ == "__main__":
    d = DequeDS()
    d.insert_front(10)
    d.insert_rear(20)
    d.insert_front(5)

    d.display()
    print("Removed from front:", d.remove_front())
    print("Removed from rear:", d.remove_rear())
    d.display()
