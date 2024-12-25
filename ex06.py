userInput1 = int(input("Enter num 1 : "))
userInput2 = int(input("Enter num 2 : "))
for i in range(userInput1,userInput2):
    if i % 3 == 0:
        if i % 5 != 0:
            print(i)
