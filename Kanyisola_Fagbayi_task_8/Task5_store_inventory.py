# Create a dictionary called store
store = {'Candles': 30, 'Bottles of Fruit wine': 150, 'Birthday cards': 150, 'Boxes of Tea': 18}


# Ask customer for their order
order = input(f"We currenlty have {store} available, please enter your order: ")
quantity = int(input("Please enter the quantity: "))

# Make a copy of the available store items
order_update = store.copy()

# Deduct the purchased item from the order
order_update[order] -= quantity 

# Print dictionary before and after purchase
print(f"Before Purchase: {store}")
after_purchase = order_update
print(f"After Purchase: {order_update}")

# Alternatively - Using update()
# Make a copy of the available store items 
order_update = store.copy()
order_update[order] -= quantity 
# Update the store item after deduction
after_purchase = store.update()

# Print dictionary before and after purchase
print(f"Before Purchase: {store}")
print(f"After Purchase: {order_update}")

