import re


with open('words.txt', 'r+') as f:
    lines = f.readlines()
    
wordlist = []
for line in lines:
    if line != "\n":
        new = line.replace("\n", "")
        if len(new) == 5:
            wordlist.append(new)

cant = input("What letters can you not use: ")
must = input("What letters must be in the word: ")
must_in_place = input("What letters are in the right place (ex: __a_b): ")

regex = ""
filtered = filter(lambda word: re.match(regex, word) != None, wordlist)
re.match(regex)

print(wordlist)