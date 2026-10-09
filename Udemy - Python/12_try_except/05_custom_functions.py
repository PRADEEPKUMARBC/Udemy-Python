def brew_chai(flavour):
    if flavour not in ["Masala", "Ginger", "Green", "Chamomile"]:
        raise ValueError(f"{flavour} is not available in the menu")
    print(f"brewing {flavour} chai ....")

brew_chai("Mint")