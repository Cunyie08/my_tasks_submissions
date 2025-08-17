# Request for five names that are spaced
names = input("Mention fives names from your class:")
# Convert to lower case
change_case = names.lower()
split_names = change_case.split()
split_names.sort()
for name in split_names:
      print(name)
print(len(name))
