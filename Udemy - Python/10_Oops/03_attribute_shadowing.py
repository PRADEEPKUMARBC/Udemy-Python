class Chai:
    temperature = "Hot"
    strength = "Strong"
    cup = "Glass"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "Small"
print("After changing", cutting.temperature)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(cutting.cup)