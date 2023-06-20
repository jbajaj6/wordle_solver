import re


with open('words.txt', 'r+') as f:
    lines = f.readlines()
    
wordlist = []
for line in lines:
    if line != "\n":
        new = line.replace("\n", "")
        if len(new) == 5:
            wordlist.append(new.lower())

print()
cant = input("What letters can you not use: ")
must = input("What letters must be in the word: ")
must_in_place = input("What letters are in the right place (ex: --a-b): ")
print()


regex = must_in_place.replace("-", ".")
wordlist = list(filter(lambda word: re.match(regex, word) != None, wordlist))

regex = ""
for letter in must:
    regex += f"(?=.*{letter})"
wordlist = list(filter(lambda word: re.match(regex, word) != None, wordlist))

regex = f"(?!.*[{cant}])"
wordlist = list(filter(lambda word: re.match(regex, word) != None, wordlist))

[print(f"{word}") for word in wordlist]
print()