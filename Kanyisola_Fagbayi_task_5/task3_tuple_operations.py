# Create a tuple of 5 Nigerian States 
Nig_states = ("Yobe", "Plateau", "Kano", "Adamawa", "Sokoto")
Five_Nig_States = tuple(Nig_states)

# Print the first and the last State
print(f"{Five_Nig_States[0]}" + " " + f"{Five_Nig_States[-1]}")

# Checking for an element in the tuple
print("Lagos" in Five_Nig_States) 
print("Lagos" not in Five_Nig_States)

# Print number of States
print(len(Five_Nig_States))