# Add input statement
nig_dish1 = input("Enter a nigerian dish:")
nig_dish2 = input("Enter a nigerian dish:")
nig_dish3 = input("Enter a nigerian dish:")

# Store them in a tuple called dishes
dishes_tuple = (nig_dish1, nig_dish2, nig_dish3)
dishes = tuple(dishes_tuple)

# Print tuple in as single line separated by commas
print(dishes)
print(",".join(dishes))

# Print each dish using new line 
print(f"{dishes[0]}\n"
f"{dishes[1]}\n"
f"{dishes[2]}\n")
