file = open("order.txt", "w")
try:
    file.write("Masal Chai 2 - cups")
finally:
    file.close()

file = open("order.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    print("Close")

with open("order.txt", "w") as file:
    file.write("Ginger Chai 3 - cups")