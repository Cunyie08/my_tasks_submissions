# Add input
days = ("Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7")
days_ = tuple(days)
# Add user input statement
activity_day1 = input("Please enter an activity:")
activity_day2 = input("Please enter an activity:")
activity_day3 = input("Please enter an activity:")
activities = {activity_day1,activity_day2,activity_day3}


# Pair each activity to a specified day using zip
specific_day = {days[0]}
day_activity = zip(specific_day,activities)
print(f"Days and Activities: {dict(day_activity)}")

# Alternatively
specific_day_activity = {days[0]: activity_day1,
            days[3]: activity_day2,
              days[-1]: activity_day3}
print(specific_day_activity)
