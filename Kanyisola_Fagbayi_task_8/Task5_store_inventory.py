# Create a dictionary called store
store = {'Candle': 30, 'Fruit wine': 150, 'Birthday cards': 150, 'Box of Tea': 18}


# Ask customer for their order
order = input(f"We currenlty have {store} available, please enter your order: ")
quantity = input("Please enter the quantity: ")

#order_keys = store.keys() == "candle"
#quantity_values = store.values() == 20


#purchase = (order_keys, quantity_values)

#for key, value in store.items():
    #print(f"Before purchase: {key}: {value}")
# Using assignment operator -

#before_prchase = store
store[order] -= quantity
print(store)
#after_purchase = (before_prchase.update())
#print(after_purchase)