# Add input Statement - names of your five best friends
best_friend1 = input("Please mention the names of fives bestfriends:")
best_friend2 = input("Please mention the names of fives bestfriends:")
best_friend3 = input("Please mention the names of fives bestfriends:")
best_friend4 = input("Please mention the names of fives bestfriends:")
best_friend5 = input("Please mention the names of fives bestfriends:")

# Store them in a tuple
names = (best_friend1, best_friend2,best_friend3, best_friend4, best_friend5)
friends = tuple(names)

# Print the tuple in reverse
print(friends[::-1])