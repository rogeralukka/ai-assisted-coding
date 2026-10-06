class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:", stack.items)
    print("Top element:", stack.peek())
    print("Removed element:", stack.pop())
    print("Stack after pop:", stack.items)
    print("Is stack empty?", stack.is_empty())
