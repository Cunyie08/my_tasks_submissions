# Create an itemlist
itemlist = []
item1 = input("Enter the name of Item 1:")
item2 = input("Enter the name of Item 2:")
item3 = input("Enter the name of Item 3:")
itemlist.append(item1)
itemlist.append(item2)
itemlist.append(item3)
print(itemlist)

# Input the values -prices
price1 = int(input("Enter the price of Item 1:"))
price2 = int(input("Enter the price of Item 2:"))
price3 = int(input("Enter the price of Item 3:"))

# Add prices to each item
storeitems = {item1: price1,
              item2: price2,
              item3: price3}
print(storeitems)

# Print available items
print(storeitems.keys())
print(storeitems.values())

# Display all items and allow user to update 
for key,value in storeitems.items():
    print(f"{key}: {value}")

storeitems.update({item1: price1,})
print(storeitems.update())

