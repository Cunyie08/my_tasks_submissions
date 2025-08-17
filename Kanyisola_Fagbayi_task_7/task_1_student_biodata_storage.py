# Ask for student biodata
name = input("Enter your name:")
age = input("Enter your age:")
gender = input("Enter your gender:")
course1 = input("Enter your course:")
course2 = input("Enter your course:")
course3 = input("Enter your course:")

courses = [course1,course2,course3]


biodata = {}
biodata["Name"] = name
biodata["Age"] = age
biodata["Gender"] = gender
biodata["Course"] = [courses]
print(biodata)

print(f"STUDENT BIODATA\nName:\t {name}\n"
f"Age:\t {age}\nGender:\t {gender}\nCourse:\t {courses}")