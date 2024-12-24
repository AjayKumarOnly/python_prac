a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))

if a < b:
    max = a
    min = b
else:
    max = b
    min = a

def gcd_fun(max,min):
    if min==0:
        return max
    else:
           return  gcd_fun(min,max % min)

ans = gcd_fun(max,min)

print(ans)
