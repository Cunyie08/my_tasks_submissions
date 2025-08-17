# Store seat numbers in a set
seat_range = set(range(1,51))
print(seat_range)

# Ask use to make a seat reservation
reserved_seat1 = int(input("Please reserve your seat, enter number:"))
# Remove seat from the set
seat_range.remove(reserved_seat1)
# Show available seats
print("Remaining seats:", seat_range)

# Ask use to make a seat reservation
reserved_seat2 = int(input("Please reserve your seat, enter number:"))
# Remove seat from the set
seat_range.remove(reserved_seat2)
# Show available seats
print("Remaining seats:", seat_range)

# Ask use to make a seat reservation
reserved_seat3 = int(input("Please reserve your seat, enter number:"))
# Remove seat from the set
seat_range.remove(reserved_seat3)
# Show available seats
print("Remaining seats:", seat_range)
