# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing ", order)
    
# prepare_chai(chai)

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Kanan Devan", "Yes", "Low") # Positional Arguments
make_chai(tea="Green", sugar="Medium", milk="No")  # Keyword arguments

def special_chai(*ingredients, **extras):
    print("Inngredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetner="Honey", foam="yes")

def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order()

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()