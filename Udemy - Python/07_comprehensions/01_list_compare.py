menu = [
    "Masala chai",
    "Ginger chai",
    "Lemon Tea",
    "Peach Tea",
]

iced_tea = [my_tea for my_tea in menu if len(my_tea) > 10]

print(iced_tea)