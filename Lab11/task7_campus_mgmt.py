class CafeteriaQueue:
    def __init__(self):
        self.orders = []

    def add_order(self, student_name, food):
        order = f"{student_name} - {food}"
        self.orders.append(order)
        print("Order added:", order)

    def serve_order(self):
        if len(self.orders) == 0:
            print("No orders to serve.")
            return
        order = self.orders.pop(0)
        print("Order served:", order)

    def display_orders(self):
        if len(self.orders) == 0:
            print("No pending orders.")
        else:
            print("Pending Orders:")
            for order in self.orders:
                print(order)


if __name__ == "__main__":
    cafeteria = CafeteriaQueue()
    cafeteria.add_order("Rahul", "Burger")
    cafeteria.add_order("Priya", "Pizza")
    cafeteria.add_order("Arjun", "Sandwich")

    print()
    cafeteria.display_orders()
    print()
    cafeteria.serve_order()
    print()
    cafeteria.display_orders()
