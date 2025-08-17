# 1. Display user details in Uppercase
text = "i love Palestine"
print(text.upper())

# 2. Print the first letter and of "python"
word = "python"
print(word[0:1])
print(word[5:])

# 3. Ask user for their name and print
user_input = str(input("What is your name?"))
name = "Anas Al-Sharif"
print(name)
print("Hello! where is the user's input?", name)

# 4. Count the number of characters without using len
text = "I used google for this solution lol!"
c = sum(1 for ch in text)
print("Number of character:", c)


# 5. Replace World with Python
word = "Hello World!"
print(word.replace("World!","Python!"))

