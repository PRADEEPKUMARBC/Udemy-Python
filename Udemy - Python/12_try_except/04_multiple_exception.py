def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity is must in number")


process_order("Ginger", 2)