# This is a simulated USSD menu interaction for a mobile clinic. 
# The products aim is to make matenrnal healthcare accessible to expectant mothers in rural areas without smartphones. 
# The end goal is to reduce maternal mortality rate in underserved regions in Nigeria.
# Grant users access to medical personnels. 
# No doubt there are a lot of infrastructure, that the govt need to put in place but this is step 1.
# Please use the prescribed prompts commented on each block.
# I have used break to stop the inputs that aren't prescribed. 
# I really enjoyed this....To be continued. #KanyisolaTheIncomingTechSisInshaAllah


print("=============================================================")
print("Q12: SIMULATED USSD MENU INTERACTION")
print("=============================================================")
# Ask user to input USSD
while True:
    ussd = str(input("Enter the USSD code:\n"))
    if ussd == "*882#":
        print("\nFor English, Press 1")
        print("For Yoruba, Press 2")
        print("For Igbo, Press 3")
        print("For Hausa, Press 4")
        print("For Pidgin, Press 5\n")
        lang_option = str(input("Please enter an option: ")) # Please enter 1, I'm still a learner...LOL
        if lang_option == "1":
            print("\nWelcome to NCC Mobile Clinic, How can we be of service to you today?:\n ")
            print("Press 1, For emergency")
            print("Press_2, For the nearest PHC")
            print("press_3, To speak with a physician")
            print("Press 00, Next")
            option = input("\nPlease select an option:")
            if option == "1":
                emergency = input("What's your emergency?: ")
                break
            elif option == "2":
                location = input("Enter your location: ")
                break
            elif option == "3":     # Please enter 3 for now.
                name = input("\nPlease enter your name: ").upper()
                nhis_no = (input("\nPlease enter your NHIS card no: "))
                if nhis_no.isdigit():
                    print(f"\nWelcome {name}, NHIS No: {nhis_no}".strip())
                else:
                    print("Invalid input. Please enter a number.")
                    break
                print("\nPress 1, to speak with the Matron")
                print("Press 2, to speak with the Gynaecologist")
                print("Press 3, to speak with the General practitioner\n")
                physician_option = (input("\nWho you would like to speak with:")) # please enter 2
                if physician_option == "1":
                    print(f"\n{name, nhis_no}, Please stay on the line while i connect you to the Matron")
                    break
                elif physician_option == "2":
                    print(f"\n{name, nhis_no}, Please stay on the line while i connect you to the Gynaecologist")
                    print(f"\nThank you for choosing our services, your call with the gynaecologist lasted for 1hr 45 mins.")
                    Matron_per_hour = 200
                    Gynaecologist_per_hour = 400
                    General_practitioner_per_hour = 300
                    Gynaecologist_per_hour *= 1.75
                    print(f"\nYour bill is:", Gynaecologist_per_hour)
                    nhis_wallet = 1500
                    if nhis_wallet >= Gynaecologist_per_hour:
                        nhis_wallet -= Gynaecologist_per_hour
                        print(f"\nTransaction successful, NHIS wallet balance is: {nhis_wallet}") 
                        print("Thank you for using our product.")
                        break
                    else:
                        print("\nInsufficient fund, Please credit your NHIS wallet")
                        break
                elif physician_option == "3":
                    print(f"{name, nhis_no}, Please stay on the line while i connect you to the General Practitioner")
                    break
                else: 
                    print("You have not selected an option.")
                    break
            elif option == "00":
                print("Press # to go back to the main menu.")
            else:
                print("You have not selected an option.")
                break
        elif lang_option == "2":
            print("E kaa bo si ile-iwosan NCC, bawo ni a se le ranyi lowo loni?: ")
            break
        elif lang_option == "3":
            print("Nnoo, i nabata NCC Clinic, kedu ka anyi nwere ike isi nyere gi aka taa?: ")
            break
        elif lang_option == "4":
            print("Barka da zuwa Asibitin NCC, ta yaya za mu iya taimaka muku a yau?: ")
            break
        elif lang_option == "5":
            print("Welcome to NCC Clinic, How we fit take help you today?: ")
            break
        else:
            print("Invalid option. Please enter correct option.")
            break
    else:
        print("Inavlid USSD!")
        break
        



