a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(a, b))

