# Create a dictionary called store
store = {'candles': 30, 'bottle of fruit wine': 150, 'birthday cards': 150, 'boxes of tea': 18}

items = store.keys()
items_qty = store.values()



while True:
    print(store)
    order = input(f"We currenlty have various items for sale, please enter your order: ")
    if order in items:
        print(f"{order} are available")
        quantity= int(input("Please enter the quantity: "))
        order_update = store.copy()
        order_update[order] -= quantity
        print(f"After Purchase: {order_update}")
        print(f"Before Purchase: {store}")
        break
    else:
        print("Item is out of stock")
        break



