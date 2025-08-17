# Collect names of guest attending a seminar
attendee1 = input("Please attendee name:")
attendee2 = input("Please attendee name:")
attendee3 = input("Please attendee name:")


# Add attendees to the set
attendees = set()
attendees.add(attendee1)
attendees.add(attendee2)
attendees.add(attendee3)
print(attendees)

# Sort the list alphabetically
attendees_order = sorted(attendees)
print("Alphabetical order of attendees", attendees_order)

