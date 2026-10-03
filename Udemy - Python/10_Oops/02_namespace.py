class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# Creating an object from the chai class

masala_tea = Chai()
print(f"{masala_tea.origin} is the origin of masala tea")
print(f"{masala_tea.is_hot} is the temperature of masala tea")

masala_tea.is_hot = False

print(f"Class: ", Chai.is_hot)
print(f"Masala {masala_tea.is_hot}" )
masala_tea.flavour = "Masala"

print(masala_tea.flavour)