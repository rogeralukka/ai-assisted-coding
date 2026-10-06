class OrderQueue:
    def __init__(self):
        self.orders = []

    def add_order(self, order_id, customer):
        order = f"{order_id} - {customer}"
        self.orders.append(order)
        print("Order added:", order)

    def process_order(self):
        if len(self.orders) == 0:
            print("No orders to process.")
            return
        order = self.orders.pop(0)
        print("Order processed:", order)

    def display_orders(self):
        if len(self.orders) == 0:
            print("No pending orders.")
        else:
            print("Pending Orders:")
            for order in self.orders:
                print(order)


if __name__ == "__main__":
    order_queue = OrderQueue()
    order_queue.add_order("ORD001", "Rahul")
    order_queue.add_order("ORD002", "Priya")
    order_queue.add_order("ORD003", "Arjun")

    print()
    order_queue.display_orders()
    print()
    order_queue.process_order()
    print()
    order_queue.display_orders()
