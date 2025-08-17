print("=============================================================")
print("Q5: DAILY MARKET REPORT")
print("=============================================================")
# Add variables
market_name = "Tejuoso Shopping Complex"
no_of_traders = 2500
daily_generated_revenue = 19568600400.90
# print request statement
print(input("Analyst: What is the name of the Market?")) # press enter
print(f"{market_name}\n")
print(input("Analyst: How many traders are in Mushin Market?")) # press enter
print(f"{no_of_traders:,}\n")
print(input("Analyst: How much is the estimated daily generated revenue in the Mushin Market")) # press enter
print(f"{daily_generated_revenue:,.2f}\n")
# Print response statement using f-string with commas
print(f"The report is about a survey carried out on a market in Lagos called {market_name}.\n"
f"{market_name} has an estimated number of {no_of_traders:,} traders,\n"
f"The market generates a daily revenue of about {daily_generated_revenue:,.2f} naira.\n")