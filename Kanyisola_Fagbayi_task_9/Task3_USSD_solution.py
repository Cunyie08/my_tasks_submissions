print("=============================================================")
print("Q12: SIMULATED USSD MENU INTERACTION")
print("=============================================================")
# Ask user to input USSD
ussd = str(input("Enter the USSD code:"))

# Add variable
ussd = "*882#"
print(f"{ussd}\n")
if ussd != "*882#":
    print("Invalid USSD!")

# Print Welcome message
print("Welcome to NCC Mobile Clinic!\n")

# Add variables

press_1 = "To get an ambulance"
press_2 = "For nearest PHC"
press_3 = "To speak with a physician"
press_00 = "next"
# Print product services
print("Please select:\n")
print(f"1. {press_1}\n2. {press_2}\n3. {press_3}\n00 {press_00}\n")
# Add user input
selection = str(input("Please enter your selection:"))
print("3\n")
# Print name details
name = input(("Please enter your name:"))
# Add variable
name = "Mrs. Okoye"
print(f"{name}\n")
# Print card details
nhis_card_no = (input("Please enter your NHIS card no:"))
# Add variable
nhis_card_no = 400057
print(f"{nhis_card_no}\n")
# Print more product services
response = str(input("Who you would like to speak with:"))
# Add variable
physician_1 = "Matron" 
physician_2 = "Gynaecologist"
physician_3 = "General practitioner"
print(f"1. {physician_1}\n2. {physician_2}\n3. {physician_3}\n")
selection = str(input("Please enter your selection:"))
print("2")
# Print display message using f-string and concatenation
print(f"\n\"The {physician_2} is currently with a patient.\"\n" + "\"Would you like me to connect you with the" + " " + f"{physician_3}.\"\n")
user_response = bool(input("Please enter True or False:"))
True == True
False == False
print(f"{True}")
# Add variable 
consultation_fee = 500
# Print transaction details
print(f"\n\"The consultation fee is ₦{consultation_fee}\"\n")
request = str(input("Would you like to proceed, Please enter True or False:"))
True == True
False == False
print(f"{False}")
# Print final statement
print("\n\"Thank you for your response, Do have a nice day\"\n")