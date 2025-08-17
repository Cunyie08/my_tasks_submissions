days = "Mondays", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
days_tuple = tuple(days)
months = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
months_tuple = tuple(months)

# Add user input 
student_name = input("What is your name?:")
gender = input("What is your gender?:")
course_track = input("What is your course track?:")
current_month_no = int(input("Enter your current month No (1-12):"))
current_day_no = int(input("Enter your current day No (1-7):"))

current_month = months[current_month_no-1] # or months [7]
current_day = days[current_day_no-1] # or months [2]

print("Attendance Tracker".center(50,"-"))
print(f"Name\t\t{student_name}\n")
print(f"Gender\t\t{gender}\n")
print(f"Course Track\t{course_track}\n")
print(f"Month\t\t{current_day}/{current_month}/2025")


