def serve_chai(flavour):
    try:
        print(f"preparing a {flavour} Chai ....")
        if flavour == "Unknown":
            raise ValueError("We don't know that flavour")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} chai is served")

serve_chai("Ginger")
serve_chai("Unknown")

number = int(input("Enter the Number: "))

try:
    result = 10/number
except ZeroDivisionError:
    print("you can not divide by zero")
except ValueError:
    print("The wasn't a valid number")
else:
    print(f"Success! the result {result}")
finally:
    print("The cleanup code is always run")