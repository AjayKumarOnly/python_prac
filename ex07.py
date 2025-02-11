  
def fibonacci(n):
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
lst=[]

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    #lst = [fibonacci(i) for i in range(1, num_terms + 1)]
    for i in range(1, 6): 
        lst.append(fibonacci(i))  
    print(lst)


