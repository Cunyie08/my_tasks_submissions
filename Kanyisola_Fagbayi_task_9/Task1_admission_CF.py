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

o_level_check_ = {o_level_subjects[0]:o_level_subjects1, o_level_subjects[1]:o_level_subjects2, o_level_subjects[2]:o_level_subjects3, o_level_subjects[3]:o_level_subjects4, o_level_subjects[-1]:o_level_subjects5}


if age >= 16:
    if utme_score >= 200:
        if uni_choice1 == "UNILAG":
            if o_level == "yes":
                if o_level_subjects1 ==  'A1'or 'B2' or 'B3'or 'C4' or 'C5' or 'C6':
                    if o_level_subjects2 ==  'A1'or 'B2' or 'B3'or 'C4' or 'C5' or 'C6':
                         if o_level_subjects3 ==  'A1'or 'B2' or 'B3'or 'C4' or 'C5' or 'C6':
                              if o_level_subjects4 ==  'A1'or 'B2' or 'B3'or 'C4' or 'C5' or 'C6':
                                   if o_level_subjects5 ==  'A1'or 'B2' or 'B3'or 'C4' or 'C5' or 'C6':
                                    print("Eligible for PUTME.")
else:
    print("Not Eligible for PUTME")


# Ask student to enter PUTME details
putme_exam = input("Did you participate for the Post UTME ('Yes' or 'No'): ")
if putme_exam == "yes":
    putme_score = int(input(f"Enter your PUTME Score: "))
    #for putme_score in range(201,321):
    if 200 <= putme_score >= 321:
        print(putme_score)
        print("Admission Granted")
    else:
        print("Not eligible for admission!!!!!")
else:
    print("Not eligible for admission")




