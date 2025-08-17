# 6. Checking for a given word (case sensitive)
text = "Python Programming"
print("python" in text)
print("Python" in text)

# 7. Write a program to reverse a string without using slicing
text = "Awesome"
def reversed_string(s):
    return "".join(reversed(s))
print(reversed_string(text))

# 8. Remove leading and trailing spaces
text = "  Palestinians are beautiful"
print(text.lstrip())
text = text = "Palestinians are beautiful  "
print(text.rstrip())

# 9. Print number of vowels in a sentence
word = input("Please enter a sentence:")
word = "I love apples and kiwi"
vowels = {'a','e','i','o','u','A','E','I','O','U'}
c = sum(1 for ch in word if ch in vowels)
print("Number of vowels:", c)

# 10. COnvert string to integer and multiply by 2
num = "1234"
print(int(str("1234"))* 2)

