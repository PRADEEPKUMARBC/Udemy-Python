class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split(",")
        return cls(tea_type.strip(), sweetness.strip(), size.strip())

order1 = ChaiOrder.from_dict({"tea_type": "Masala", "sweetness": "Medium", "size": "Large"})
print(order1.tea_type, order1.sweetness, order1.size)  # Output: Masala Medium Large

order2 = ChaiOrder.from_string("Green, Low, Small")
print(order2.tea_type, order2.sweetness, order2.size)  #

order3 = ChaiOrder("Large", "Low", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)