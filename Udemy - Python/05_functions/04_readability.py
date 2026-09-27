def calculate_bill(cups, price_per_cup, tax_rate):
    subtotal = cups * price_per_cup
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

print(calculate_bill(3, 2.5, 0.07))