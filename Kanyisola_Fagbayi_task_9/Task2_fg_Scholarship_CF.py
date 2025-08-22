# Federal Government Scholarship 

# Ask for the applicant's Basic Info
name = input("Enter your name: ").upper()
gender = input("Enter your gender: ").upper()


# Checking for qualification
while True:
    age = int(input("Enter your age: "))
    if (age >= 16):
        score = score = int(input("Enter your score: "))
        if (score >= 70):
            citizen = input("Are you from Nigeria? True or False: ")
            if (citizen == "yes"):
                Undergraduate_student = input("Are you a full time undergraduate student from a recognised Nigerian university? Yes or No:")
                if (Undergraduate_student == "yes"):
                    other_student_scho = input("Do you have a scholarship from any Oil and Gas Industry (local or international)? Yes or No: ")
                    if (other_student_scho == "no"):
                        academic_subjects = input("Enter five subjects including Maths and English: ").split()
                        academic_result1= input(f"Enter the result for {academic_subjects[0]}: ").upper()
                        academic_result2= input(f"Enter the result for {academic_subjects[1]}: ").upper()
                        academic_result3= input(f"Enter the result for {academic_subjects[2]}: ").upper()
                        academic_result4= input(f"Enter the result for {academic_subjects[3]}: ").upper()
                        academic_result5= input(f"Enter the result for {academic_subjects[-1]}: ").upper()
                        results = ((academic_result1) and (academic_result2) and (academic_result3) and (academic_result4) and (academic_result5))
                        if ((results == 'A1') or (results == 'B2') or (results == 'B3')):
                            print(f"{name}, You are eligible for Scholarship!.")
                            break
                        else:
                            print(f"{name}, You do not possess the required grade. Not eligible!")
                            break
                    else:
                        print(f"{name}, You cannot apply for another scholarship!")
                        break
                else:
                    print(f"{name}, Only full time students are eligible!.")
                    break
            else:
                print(f"{name}, You are not eligible! You must be a citizen to qualify.")
                break
        else:
            print("You do not met the score requirement")
            break
    else:
        print("You do not met the age requirement")
        break




# student_file = {
#     "Basic Info": {
#         "Name": name,
#         "Age": age,
#         "Gender": gender,
#         "Nationality": citizen
#     },
#     "Academic Info": {
#         "Score": score,
#         "Enrollment": Undergraduate_student,
#         "Other Scholarships": other_student_scho,
#         "Subjects": academic_subjects,
#         "Results": academic_result_check
#     },
#}


# academic_result_check = {academic_subjects[0]:academic_result1, academic_subjects[1]:academic_result2, academic_subjects[2]:academic_result3, academic_subjects[3]:academic_result4, academic_subjects[-1]:academic_result5}
# results = ((academic_result1) and (academic_result2) and (academic_result3) and (academic_result4) and (academic_result5))



