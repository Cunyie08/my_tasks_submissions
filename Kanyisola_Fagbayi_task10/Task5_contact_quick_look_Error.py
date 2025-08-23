# To run each error code... comment the other code out first

# Using TRY-EXCEPT for NameErrors
user_names = []
user1 = input("Please enter your name:")
user2 = input("Please enter your name:")
user3 = input("Please enter your name:")

# Comment out to see the error message
# try: 
#     print(user11)
# except NameError:
#     print("users1 not defined")

# Create an empty list and ask users for their numbers
user_nums = []
user_num1 = (input("Please enter your phone number:"))
user_num2 = (input("Please enter your phone number:"))
user_num3 = (input("Please enter your phone number:"))

# Add user numbers to the empty list
user_nums.append(user_num1)
user_nums.append(user_num2)
user_nums.append(user_num3)

# Convert list of user numbers to tuple
user_nums_tuple = tuple(user_nums)
print(user_nums_tuple)

# Using TRY-EXCEPT for TypeErrors
try:
    print(user_nums_tuple = "ABC" + 12345)
except TypeError:
    print("str and int not allowed")
