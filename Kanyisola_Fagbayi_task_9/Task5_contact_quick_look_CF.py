# Create an empty list and ask users for their names
user_names = []
user1 = input("Please enter your name:")
user2 = input("Please enter your name:")
user3 = input("Please enter your name:")

# Add usernames to the empty list
user_names.append(user1)
user_names.append(user2)
user_names.append(user3)
user_names_tuple = tuple(user_names)

# Convert list of usernames to tuple
print(user_names_tuple)

# Create an empty list and ask users for their numbers
user_nums = []
user_num1 = int(input("Please enter your phone number:"))
user_num2 = int(input("Please enter your phone number:"))
user_num3 = int(input("Please enter your phone number:"))

# Add user numbers to the empty list
user_nums.append(user_num1)
user_nums.append(user_num2)
user_nums.append(user_num3)

# Convert list of user numbers to tuple
user_nums_tuple = tuple(user_nums)
print(user_nums_tuple)

# Create a dictionary from the details collected
contact_info = dict(zip(user_names_tuple,user_nums_tuple))
print(contact_info)

# Using While loop to fetch user info from the dictionary
while True:
    username_search = input("Please enter a user name:")
    if ((username_search == user1) or (username_search == user2) or (username_search == user3)):
        print(f"({username_search}) is a contact")
        usernum_search = int(input("Please enter a user number:"))
        if ((usernum_search == user_num1) or (usernum_search == user_num2) or (usernum_search == user_num3)):
            print(f"{username_search} - ({usernum_search}) is a contact")
            print(contact_info)
            break
        else:
            print("Contact not found")
            break
    else:
        print("User does not exist")
        break