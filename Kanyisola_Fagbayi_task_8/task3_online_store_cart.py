# Create a list of Items
store_items = ["Candle", "Chocolate","Biscuit", "Diffuser"]
store_items_prices = [10000, 5000, 4000, 40000]

# Add prices to items
Candle = (store_items_prices[0])
Diffuser = (store_items_prices[-1])
Chocolate = (store_items_prices[1])
Biscuit = (store_items_prices[2])

# Create an Empty cart and add purchased items
Shopping_cart_total = 0
Shopping_cart_total += Candle
Shopping_cart_total += Biscuit
Shopping_cart_total += Chocolate
Shopping_cart_total += Diffuser

# Check out with the list of items purchased
print(f"Items Sold:\t{store_items}\nTotal Amount:\t{Shopping_cart_total}")

# Customer wants to take out an item from the cart
Shopping_cart_total -= Biscuit
print(f"Items Sold:\t{store_items[0]},{store_items[1]},{store_items[-1]}\nNew Total:\t{Shopping_cart_total}")

