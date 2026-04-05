'''
Take a sentence from the user.
Count words, replace a word, join words with a separator, and find a specific word.
'''

sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()
print("Words in sentence:", words)
print("Number of words:", len(words))

# Replace a word
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
new_sentence = sentence.replace(old_word, new_word)
print("After replacement:", new_sentence)

# Join words with a hyphen
joined_sentence = "-".join(words)
print("Joined sentence with '-':", joined_sentence)

# Find a word
search_word = input("Enter word to find: ")
position = sentence.find(search_word)
if position != -1:
    print(f"'{search_word}' found at index:", position)
else:
    print(f"'{search_word}' not found")