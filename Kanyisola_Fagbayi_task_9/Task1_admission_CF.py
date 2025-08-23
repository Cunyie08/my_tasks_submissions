# Ask for the applicant's Basic Info
name = input("Enter your name: ").upper()
gender = input("Enter your gender: ").upper()


# Ask student for University choice
# Ask student to input number of WASSCE sitting
# Ask student to enter subjects and the reults

while True:
    age = int(input("Enter your age: "))
    if age >= 16:
        utme_score = int(input("Enter your UTME score: "))
        if utme_score >= 200:
            uni_choice1 = input("Enter your University first choice: ")
            uni_choice2 = input("Enter your University second choice: ")
            uni_choice3 = input("Enter your University third choice: ")
            if uni_choice1 == "UNILAG":
                o_level = input("Do you have an O'level result from one sitting ('Yes' or 'No'): ")
                if o_level == "yes":
                    o_level_subjects = input("Enter five relevant subjects including Maths and English: ").split()
                    o_level_subjects1= input(f"Enter the result for English ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
                    o_level_subjects2= input(f"Enter the result for Maths: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
                    o_level_subjects3= input(f"Enter the result for {o_level_subjects[2]}: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
                    o_level_subjects4= input(f"Enter the result for {o_level_subjects[3]}: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
                    o_level_subjects5= input(f"Enter the result for {o_level_subjects[-1]}: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
                    o_level_results = ((o_level_subjects1) and (o_level_subjects2) and (o_level_subjects3) and (o_level_subjects4) and (o_level_subjects5))
                    if ((o_level_results == 'A1') or (o_level_results == 'B2') or (o_level_results == 'B3') or (o_level_results == 'C4') or (o_level_results == 'C5') or (o_level_results == 'C6')):
                        putme_exam = input("Did you participate for the Post UTME ('Yes' or 'No'): ")
                        if putme_exam == "yes":
                            putme_score = int(input(f"Enter your PUTME Score: "))
                            if ((putme_score >= 200) or (putme_score == 321)):
                                print(putme_score)
                                print("Admission Granted")
                                break
                            else:
                                print("Not eligible for admission!!!!!")
                                break
                        else:
                            print("Not eligible for admission")
                            break 
                        print("Eligible for PUTME.")
                        break
                    else:
                        print("Not Eligible for PUTME")
                        break
                else:
                    print("Not Eligible for PUTME")
                    break
            else:
                print("Not Eligible for PUTME")
                break
        else:
            print("Not Eligible for PUTME")
            break
    else:
        print("Not Eligible for PUTME")
        break






