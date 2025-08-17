# Add user input
name = input("What is your name?:")
age = input("What is your DOB?:")
favorite_color = input("What is your favorite color?:")
Hometown = input("Where is your hometown?:")

user_details = (name, age, favorite_color, Hometown)
user_tuple = tuple (user_details)
name = user_tuple[0]
age = user_tuple[1]
favorite_color = user_tuple[2]
Hometown = user_tuple[3]

# Print and align infomation using escape sequence
print(f"Name\t\t{name}\nAge\t\t{age}\nFavorite Color\t{favorite_color}\nHometown\t{Hometown}")



