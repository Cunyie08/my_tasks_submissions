# Ask user to enter a word

word = input("Please enter the longest word you know: ")

try:
    word = int("Hippotamus")
except ValueError:
    print("Cannot convert str to int")
finally:
    print("Traceback")
    

# # Define the vowels 
# vowels = 'a','e','i','o','u','A','E','I','O','U'
# vs = sum(1 for char in word if char in vowels)
# print(f"There are {vs} vowel(s) in the word")
