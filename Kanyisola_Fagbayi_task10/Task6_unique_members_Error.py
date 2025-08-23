# Add user input
member1 = input("Please enter your name:").split(",")
member2 = input("Please enter your name:").split(",")
member3 = input("Please enter your name:").split(",")


#Convert the names of the member to set
member1_set = set(member1)
member2_set = set(member2)
member3_set = set(member3)
print(set.union(member1_set,member2_set,member3_set)) #print("Here are the names:", ",".split(names_list))


# Create a dictionary where each name is key and value is length
unique_member1 = {name: len(name) for name in member1_set}
unique_member2 = {name: len(name) for name in member2_set}
unique_member3 = {name: len(name) for name in member3_set}


## Using TRY-EXCEPT for KeyError and IndexError
try:
    print(unique_member1["gender"])
except KeyError:
    print("Key not found")


unique_members = (unique_member1, unique_member2, unique_member3)
try:
    unique_members[3]
except IndexError:
    print("Index out of range")



