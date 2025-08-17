print("=======================================================")
print("Q11: NIGERIAN CURRENCY CONVERTER")
print("=======================================================")
# Add variables
naira_value = 2000000.00
naira_to_USD = 1550.45
naira_to_GBP = 2050.32
USD_to_naira = 1300.25
GBP_to_naira = 1950.65


# Ask for inputs
exch_naira = (input("How much naira do you have?:")) # press enter
print(input((f"₦{naira_value:,.2f}")))
USD_exch_rate = (input("What is the dollar exch rate today?:")) # press enter
print(f"${naira_to_USD:,.2f}")
GBP_exch_rate = (input("What is the pounds exch rate today?:")) # press enter
print(f"£{naira_to_GBP:,.2f}")
# conversion to naira value
naira_USD_exch = (input(f"How much is ₦{naira_value:,.2f} in dollars?:")) # press enter
naira_USD_exch = naira_value // naira_to_USD
print(f"${naira_USD_exch:,.2f}")
naira_GBP_exch = (input(f"How much is ₦{naira_value:,.2f} in pounds?:")) # press enter
naira_GBP_exch = naira_value // naira_to_GBP
print(f"£{naira_GBP_exch}")
# print output statement with f"{value:.2f}""
print(f"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"\n\t\tACCESSIBILTY BANK PLC")
print(f"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"\n\t\tExchange Rates")
print(f"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"\nDate\t\t\t\tTime")
print(f"\n08/08\t\t\t\t09:00")
print(f"\n\t\t\tWE BUY AT\t\tWE SELL AT")
print(f"\n $\t\t\t₦{USD_to_naira:,.2f}\t\t₦{naira_to_USD:,.2f}")
print(f"\n £\t\t\t₦{GBP_to_naira:,.2f}\t\t₦{naira_to_GBP:,.2f}")
print(f"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"Dollar exchange value:\t${naira_USD_exch:,.2f}")
print(f"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"Pounds exchange value:\t£{naira_GBP_exch:,.2f}")
print(f"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
