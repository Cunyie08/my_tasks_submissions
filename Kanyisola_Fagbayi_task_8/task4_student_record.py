# Create an empty dictionary
students = {}

# Student record - Ask student to enter their name, age, gender and courses
name = input("Please enter your full name: ").title()
age = int(input("Please enter your age: "))
gender = input("please enter your gender: ").capitalize()
courses = ["Physics", "Maths", "English", "Biology"]

# Data
scores = [63, 45, 60]
average_scores = sum(scores)/len(scores)
print(average_scores)



# Use comparison operator to check student age category and grade 
teenager = age <= 19 
GradeA = (average_scores >= 65) 
Passed = (GradeA == True)


# Store student details in a dictionary
students = {
    "Basic Info": {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Courses": courses  
    },
    "Scores": scores,

    "Passed": {Passed}
}


# Print the Student Complete record using f-strings
print(f"------------------Students' Record---------------------")
print(f"Student Name:\t{students["Basic Info"]["Name"]}")
print(f"Age:\t\t{students["Basic Info"]["Age"]}")
print(f"Gender\t\t{students["Basic Info"]["Gender"]}")
print(f"Teenager\t{teenager}")
print(f"Subjects\t{'|'.join(students["Basic Info"]["Courses"])}")
print(f"Results\t\t{students["Scores"]}")
print(f"Average Score:\t{average_scores}")
print(f"Passed:\t\t{Passed}")

