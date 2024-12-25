read_line = "read.txt"
write_line = "write.txt"

file = open(read_line,"r")
data = file.read()
file.close()

with open(write_line,"a") as file:
    file.write(data)
    print("Data Transferred")
wordCount = len(data.split())
print(f"The Number of count is -> {wordCount}")