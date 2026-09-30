Tea_Price_INR = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_price_usd = { tea:price /80 for tea, price in Tea_Price_INR.items()}
print(tea_price_usd)