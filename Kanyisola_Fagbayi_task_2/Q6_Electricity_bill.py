print("=========================================================")
print("Q6: ELECTRICITY BILL FORMATTER")
print("=========================================================")
#Ask for input
print(input("Enter your full name:")) # press enter
# Add variables
customers_full_name = "Apartment 2D"
print(f"{customers_full_name}\n")
#Ask for input
print(input("Enter the units consumed:")) # press enter
# Add variables
units_consumed = 100
print(f"{units_consumed}\n")
#Ask for input
print(input("Enter the cost per unit:")) # press enter
# Add variables
cost_per_unit = 251.64
print(f"₦{cost_per_unit}\n")
# Prorate the bill
vat = 75/100 * cost_per_unit * units_consumed
total_bill = units_consumed * cost_per_unit + vat
# print output statement with Newlines
print("===================================")
print("\tElectricity bill")
print("===================================")
print("Month:\t\tJune-July 2025\n\nCustomer ID:\t", customers_full_name,"\n\n"
"Units consumed:\t", units_consumed, "\n\n""Rate(₦):\t",cost_per_unit, "\n\n"
"VAT(₦):\t\t", (f"{vat:,.2f}"))
print("===================================")
print("Amount Due(₦):\t", (f"{total_bill:,.2f}"))
print("===================================")