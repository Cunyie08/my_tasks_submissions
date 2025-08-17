# Add input statement
word = input("Enter a word of your choice:")
# print the length of the word
print(len(word))
# Check if the word is in the uppercase or lowercase or titlecase
print(word.upper() in word)
print(word.lower() in word)
# Reverse the word using slicing
print(word[::-1])