# favourite_chais = [
#     "Masala Chai", "Green Tea", "Masala Chai",
#     "Lemon tea", "Green Tea", "Elaichi tea"
# ]

# unique_chai = { chai for chai in favourite_chais if len(chai) > 6 }
# print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardmom", "clove"],
    "Elaichi chai": ["cardmom", "milk"],
    "Spicy chai": ["ginger", "Black papper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)