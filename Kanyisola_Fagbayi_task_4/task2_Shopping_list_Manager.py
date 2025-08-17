# Create an Empty list
shopping_list = []
item1 = input("Enter selected item: ")
item2 = input("Enter selected item: ")
item3 = input("Enter selected item: ")

# Append the empty list (shopping_list)
shopping_list.append(item1)
shopping_list.append(item2)
shopping_list.append(item3)

# Display output as a string separated by commas 
print("Here is the shopping list:", ",".join(shopping_list))
