def isArmstrong(num):
    copy = num
    digit = 0
    while(copy > 0):
        digit=digit +1
        copy = copy // 10

    sum = 0
    copy = num

    while(copy>0):
        sum = sum + pow(copy%10,digit)
        copy //= 10
    return sum == num

userInput = int(input("Enter the Number : "))

if isArmstrong(userInput):
    print(f"{userInput} is a Armstrong number")
else:
    print(f"{userInput} is not a Armstrong number")



