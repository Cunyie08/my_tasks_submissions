# Ask for the applicant's Basic Info
name = input("Enter your name: ").upper()
age = int(input("Enter your age: "))
gender = input("Enter your gender: ").upper()
utme_score = int(input("Enter your UTME score: "))

# Ask student for University choice
uni_choice1 = input("Enter your University first choice: ")
uni_choice2 = input("Enter your University second choice: ")
uni_choice3 = input("Enter your University third choice: ")

# Ask student to input number of WASSCE sitting
o_level = input("Do you have an O'level result from one sitting ('Yes' or 'No'): ")

# Ask student to enter subjects and the reults
o_level_subjects = input("Enter five relevant subjects including Maths and English: ").split(",")
o_level_subjects1= input(f"Enter the result for English ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
o_level_subjects2= input(f"Enter the result for Maths: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
o_level_subjects3= input(f"Enter the result for {o_level_subjects[2]}: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
o_level_subjects4= input(f"Enter the result for {o_level_subjects[3]}: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
o_level_subjects5= input(f"Enter the result for {o_level_subjects[-1]}: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()

# Ask student to enter PUTME details
putme_exam = input("Did you participate for the Post UTME ('Yes' or 'No'): ")
putme_score = int(input("Enter your PUTME score: "))

# Using logical operator to confirm if a student's result is eligible
results1 = (((o_level_subjects1 == "A1") or (o_level_subjects1 == "B2")) or ((o_level_subjects1 == "B3") or (o_level_subjects1 == "C4")) or ((o_level_subjects1 == "C5") or (o_level_subjects1 == "C6")))
results2 = (((o_level_subjects2 == "A1") or (o_level_subjects2 == "B2")) or ((o_level_subjects2 == "B3") or (o_level_subjects2 == "C4")) or ((o_level_subjects2 == "C5") or (o_level_subjects2 == "C6")))
results3 = (((o_level_subjects3 == "A1") or (o_level_subjects3 == "B2")) or ((o_level_subjects3 == "B3") or (o_level_subjects3 == "C4")) or ((o_level_subjects3 == "C5") or (o_level_subjects3 == "C6")))
results4 = (((o_level_subjects4 == "A1") or (o_level_subjects4 == "B2")) or ((o_level_subjects4 == "B3") or (o_level_subjects4 == "C4")) or ((o_level_subjects4 == "C5") or (o_level_subjects4 == "C6")))
results5 = (((o_level_subjects5 == "A1") or (o_level_subjects5 == "B2")) or ((o_level_subjects5 == "B3") or (o_level_subjects5 == "C4")) or ((o_level_subjects5 == "C5") or (o_level_subjects5 == "C6")))
results = ((results1) and (results2) and (results3) and (results4) and (results5))

# Dictionary input
students = {
    'Basic info:': {
        'Name': name,
        'Age' : age,
        'Gender' : gender,
    },
        'Academics': {
            'Utme Score': utme_score >= 200,
            'Uni First choice' : uni_choice1 == "UNILAG",
            'O-level sitting' : o_level == "yes",
            'O-level subjects' : o_level_subjects,
            'O-level results' : results,
            'PUTME Exam' : putme_exam == "yes",
            'PUTME Score': putme_score >= 200,
},
}

# Check for eligibilty 
eligibility = (age >= 16) and (utme_score >= 200) and (uni_choice1 == "UNILAG") and (o_level == "yes") and (putme_exam == "yes") and (putme_score >= 200) and (results == True)

# Print Output 
print(f"Name:\t{name}\nAge:\t\t{age}")
print(f"Gender:\t\t{gender}\nUTME Score:\t{utme_score}")
print(f"One sitting:\t{o_level}")
print(f"O'level sub:\t{o_level_subjects:}")
print(f"O'Level result:\t{results}\nPUTME:\t\t{putme_exam}")
print(f"PUTME Score:\t{putme_score}\nEligibilty:\t{eligibility}")






