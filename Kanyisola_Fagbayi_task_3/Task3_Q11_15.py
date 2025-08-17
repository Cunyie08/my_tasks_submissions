# 11. Spliting a given word
word = "apple,banana,orange"
print(word.split())

# 12. Ask a user for a semtemce and print each word using\n
text = input("Can you form a sentence with love?:")
sentence = "I\nlove\nBarcelona's\nnew\njersey"
print(sentence)

# 13. Replace al spaces in a string with (_)
text = "Palestine will be free insha Allah"
print(text.replace(" ", "_"))

# 14. Count the letter 'a' in Banana
text = "banana"
letter_a = {'a'}
c = sum(1 for ch in text if ch in letter_a)
print("Number of 'a' in Banana:", c)

# 15. Check if a string starts with "https://"
url = "https://"
print("http://" in url)
print("https://" in url)