# Add input statement - user shopping list
s_item1 = input("Enter your shopping list: ")
s_item2 = input("Enter your shopping list: ")
s_item3 = input("Enter your shopping list: ")

# Store tuple
shopping_list = (s_item1,s_item2,s_item3)
shopping_list_tuple = tuple(shopping_list)

# convert tuple to list
lst = list(shopping_list_tuple)
print(lst)

# Ask for two more items
s_item4 = input("Enter your shopping list: ")
s_item5 = input("Enter your shopping list: ")

# Append the items
lst.append(s_item4)
lst.append(s_item5)

# Convert list back to tuple and print
t = tuple(lst)
print(t)


# Display output - updated list separated by | 
print("Here is the updated shopping list:", "|".join(t))
