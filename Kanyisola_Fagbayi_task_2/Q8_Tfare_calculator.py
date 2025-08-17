print("============================================================")
print("Q8: TRANSPORT FARE CALCULATOR")
print("============================================================")
# Ask for inputs
dist_in_km = (input("What is the distance to Heathrow:")) # press enter
# Add variables
dist_in_km = 69
print(f"{dist_in_km}km")
fare_per_km_usd = (input("What is the base fare:")) # press enter
# Add variables
fare_per_km = 5.0
print(f"${fare_per_km}")
# Calculate the total fare
total_fare = dist_in_km * fare_per_km
# print output statement with f"{value:.2f}""
print(f"To estimate the total cost of the trip, multiply the distance which is {dist_in_km}km by the base fare (${fare_per_km}). Total fare is ${total_fare:.2f}")