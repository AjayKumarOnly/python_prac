file = open("read.txt","r")

all = file.read()

vowelCount = 0
spaceCount = 0
charCount = 0
lineCount = 0
for i in all:
    if i.lower() in "aeiou":
        vowelCount += 1
    if i.isspace():
        spaceCount += 1
    if i == '\n':
        lineCount += 1
    charCount+=1

print(f"vowelCount : {vowelCount}")
print(f"spaceCount : {spaceCount}")
print(f"charCount : {charCount}")
print(f"Line count : {lineCount}")
