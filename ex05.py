userInput = "Python Programming "

vowelCount = 0
spaceCount = 0
charCount = 0
for i in userInput:
    if i.lower() in "aeiou":
        vowelCount += 1
    elif i.isspace():
        spaceCount += 1
    charCount+=1

print(f"vowelCount : {vowelCount}")
print(f"spaceCount : {spaceCount}")
print(f"charCount : {charCount}")