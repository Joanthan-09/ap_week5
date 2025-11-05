# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'


magic= "abracadabra"

print(magic[5:6])
print(magic[9:10])
print(magic[4:5])


# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet =  "abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13])

# c. Reverse the entire string using slicing.
rev_alphabet = alphabet[::-1]
print(rev_alphabet)



# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

hyphen_index = quote.rfind("-")

name = quote[hyphen_index + 1:].strip()

print(f"The extracted name is: {name}")

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

info = "Python is fun. Fun is good. Good is subjective."

print(info.rfind('subjective'))

subjective_word = info[36:]

print(subjective_word)

ever_third_word = info.split()[::-1]

rev_word_pos = info.split()[::-1]

rev_word_pos = ''.join(rev_word_pos)



# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text = "MAY THE FORCE BE WITH YOU."
lowercase_text = text.lower()
print(lowercase_text)


# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
motto_string = ' '.join(motto)
# b. Now, split the string at every occurrence of the letter 'a'.
split_motto = motto_string.split('a')

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
sentence ="Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.