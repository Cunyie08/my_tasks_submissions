# Create an empty dictionary
students = {}

# Student record - Ask student to enter their name age and scores
name = input("Please enter your full name: ").title()
age = int(input("Please enter your age: "))
gender = input("please enter your gender: ").capitalize()
courses = ["Physics", "Maths", "English", "Biology"]

# Data
physics = 45
maths = 75
english = 70
biology = 90

# Use comparison operator to check student age category and grade 
teenager = age <= 19 #== True
passed_phys = (physics >= 65)
passed_maths = (maths >= 65) 
passed_eng = (english >= 65)
passed_bio = (biology >= 65)


# Store student details in a dictionary
students = {
    "Basic Info": {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Courses": courses  
    },
    "Scores": [physics, maths, english, biology],

    "Passed": {
        "passed_Phys" : True,
        "passed_maths" : True,
        "passed_english" : True,
        "passed_biology" : True,
    }
}



# Print the Student Complete record using f strings
print(f"------------------Students' Record---------------------")
print(f"Student Name:\t{students["Basic Info"]["Name"]}")
print(f"Age:\t\t{students["Basic Info"]["Age"]}")
print(f"Gender\t\t{students["Basic Info"]["Gender"]}")
print(f"Teenager\t{teenager}")
print(f"Subjects\t{'|'.join(students["Basic Info"]["Courses"])}")
print(f"Results\t\t{students["Scores"]}")
print(f"Passed Phys:\t{passed_phys}")
print(f"Passed Maths:\t{passed_maths}")
print(f"Passed Eng.:\t{passed_eng}")
print(f"Passed Bio.:\t{passed_bio}")
