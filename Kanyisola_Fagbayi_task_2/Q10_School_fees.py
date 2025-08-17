print("======================================================")
print("Q10: SCHOOL FEES BREAKDOWN")
print("======================================================")

# Ask for inputs
institution = "University of Abeokuta"
student_full_name = (input("Can I have your name please:")) # press enter
# Add variables
student_full_name = "John Legend"
print(student_full_name)
tuition_fee = (input("Enter your tuition fee:")) # press enter
# Add variables
tuition_fee = 44999.99
print(f"₦{tuition_fee:,.2f}")
hostel_fee = (input("Enter your hostel fee:")) # press enter
# Add variables
hostel_fee = 25499.99
print(f"₦{hostel_fee:,.2f}")
feeding_fee = (input("Enter your feeding fee:")) # press enter#
# Add variables
feeding_fee = 20000.00
print(f"₦{feeding_fee:.2f}")
# Calculate total amount
total_due = tuition_fee + hostel_fee + feeding_fee
# print output statement
print(f"+++++++++++++++++++++++++++++++++++++++++++++")
print(f"\t {institution}")
print(f"+++++++++++++++++++++++++++++++++++++++++++++")
print(f"\t\tSchool bill")
print(f"+++++++++++++++++++++++++++++++++++++++++++++")
print(f"\nSemester:\t\tSecond semester")
print(f"\nSession:\t\t2025/2026")
print(f"Student Name:\t\t{student_full_name}")
print(f"Tuition Fee(₦):\t\t{tuition_fee:,.2f}")
print(f"Hostel fee(₦):\t\t{hostel_fee:,.2f}")
print(f"Feeding fee(₦):\t\t{feeding_fee:,.2f}")
print(f"+++++++++++++++++++++++++++++++++++++++++++++")
print(f"Total Amount Due(₦):\t{total_due:,.2f}")
print(f"+++++++++++++++++++++++++++++++++++++++++++++")


