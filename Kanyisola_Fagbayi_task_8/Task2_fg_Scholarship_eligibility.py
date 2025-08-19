# Ask the student for their name, age and score
#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#score = int(input("Enter your score: "))

# Check if the student is eligible for a scholarship
#eligibility = (age < 18) and (score > 70)
#print(f"Candidate: {name}\n Age: {age}\n Score: {score}\n Eligibility: {eligibility}")

# Explanation
print("""The code above is checking for eligibility. A student is eligible for scholarship
if he/she is younger or aged 18 with a requirement score of 70 or above. 
If the conditions are not met (False); the studenet is not eligible to apply. 
If the conditions are met (True); the studenet is eligible to apply for a scholarship.
""")

# Federal Government Scholarship 
# Ask for the applicant's Basic Info
name = input("Enter your name: ").upper()
age = int(input("Enter your age: "))
score = int(input("Enter your score: "))
citizenship = input("Are you from Nigeria? Yes or No: ")

# Ask applicant for academic details
Undergraduate_student = input("Are you a full time undergraduate student from a recognised Nigerian university? Yes or No:")
other_student_scho = input("Do you have a scholarship from any Oil and Gas Industry (local or international)? Yes or No: ")
academic_subjects = input("Enter five subjects including Maths and English: ").split()
academic_result1= input(f"Enter the result for {academic_subjects[0]}: ").upper()
academic_result2= input(f"Enter the result for {academic_subjects[1]}: ").upper()
academic_result3= input(f"Enter the result for {academic_subjects[2]}: ").upper()
academic_result4= input(f"Enter the result for {academic_subjects[3]}: ").upper()
academic_result5= input(f"Enter the result for {academic_subjects[-1]}: ").upper()
academic_result_check = {academic_subjects[0]:academic_result1, academic_subjects[1]:academic_result2, academic_subjects[2]:academic_result3, academic_subjects[3]:academic_result4, academic_subjects[-1]:academic_result5}

# Use assignment and logic Operator to assign and combine conditional statements respectively
results = (((academic_result1 == "A") or (academic_result1 == "B")) and ((academic_result2 == "A") or (academic_result2 == "B")) and ((academic_result3 == "A") or (academic_result3 == "B")) and ((academic_result4 == "A") or (academic_result4 == "B")) and ((academic_result5 == "A") or (academic_result5 == "B")))


# Check if the student is eligible for the Scholarship
eligibility = (age >= 18) and (score >= 70) and (citizenship == "yes") and (Undergraduate_student == "yes") and (other_student_scho == "no") and (results == True) # (results == "B")
print(f"Candidate:\t{name}\n Age:\t{age}\n Score:\t{score}\n Citizenship:\t{citizenship:}"
f"Full-time Undergraduate student:\t{Undergraduate_student}\n Other Scholarships:\t{other_student_scho}"
f"WASSCE Result:\t{academic_result_check}\n Eligibilty:\t{eligibility}")


