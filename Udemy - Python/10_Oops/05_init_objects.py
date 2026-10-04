class ChaiOrder:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"Order: {self.size} ml of {self.type} Chai"

order_one = ChaiOrder("Masala", 150)
print(order_one.summary())

order_two = ChaiOrder("Ginger", 200)
print(order_two.summary())