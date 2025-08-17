# Create a list of five cities 
list= input("Mention five cities in England:")
list_of_cities = ['Bath', 'York', 'London', 'Bristol', 'Leeds']

# Replace third city with a new one
list_of_cities [2] = 'Chelmsford'
print(list_of_cities)

# Remove the last city
last_list = list_of_cities.pop()
print(last_list)
print(list_of_cities)

# Add a new city to the beginning of the list
list_of_cities.insert(0, "Manchester")

# Print updated list
print(list_of_cities)
