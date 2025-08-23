# Ask user to enter a word
word = input("Please enter the longest word you know: ")

# Define the vowels 
vowels = 'a','e','i','o','u','A','E','I','O','U'
vs = sum(1 for char in word if char in vowels)
print(f"There are {vs} vowel(s) in the word")

