# Create two empty lists
students_names = []
students_scores = []

# Request for students's name
student_name1 = input("Enter your name:")
student_name2 = input("Enter your name:")
student_name3 = input("Enter your name:")

# Append the empty list (students_names)
students_names.append(student_name1)
students_names.append(student_name2)
students_names.append(student_name3)
print(students_names)

# Request for Student's score 
student_score1 = input("What did you score " f"{student_name1}?")
student_score2 = input("What did you score " f"{student_name2}?")
student_score3 = input("What did you score " f"{student_name3}?")

# Append the empty List (students_scores)
students_scores.append(student_score1)
students_scores.append(student_score2)
students_scores.append(student_score3)

# Using f string to print the output
print(f"Name\tScore\n{student_name1}\t{student_score1}\n{student_name2}\t{student_score2}\n{student_name3}\t{student_score3}")

# Using indexing to print the output
print
print(f"Name\tScore\n{students_names[0]}\t{students_scores[0]}")
print(f"{students_names[1]}\t{students_scores[1]}")
print(f"{students_names[2]}\t{students_scores[2]}")







