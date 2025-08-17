# Collecting Unique Voters registration details
voters = set()

# Ask Voter for their imput
voter1 = input("Please enter your name:")
voter2 = input("Please enter your name:")
voter3 = input("Please enter your name:")
name = input("Please enter your name:")

# Adding voters names
voters.add(voter1)
voters.add(voter2)
voters.add(voter3)
print(voters)
if name in voters:
    print(f"Warning: Duplicate entry - this user has been registered.")
else:
    voters.add(name)
    print(f"Unique Voters: {voters}")

# Print Total number of unique voters
print("Total no of unique voters:", len(voters))


