year = int(input("Enter the Year : "))

if(year % 100 == 0 and year % 400 == 0):
    print(f"Year {year} is a Leap Year")
elif(year % 4 ==0 and year % 100 != 0):
    print(f"Year {year} is a Leap Year")
else:
    print(f"Year {year} is not a Leap Year")
