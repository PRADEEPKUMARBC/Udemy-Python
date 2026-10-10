class InvalidChaiError(Exception):
    pass

def bill(flavour, cups):
    menu = {"Masala":20, "Ginger":40}
    try:
        if flavour not in menu:
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavour] * cups
        print(f"your bill for {cups} cups for {flavour} chai: rupees {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting our chai shop")

bill("Mint", 30)
bill("Ginger", 20)