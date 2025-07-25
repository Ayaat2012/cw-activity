import math

def prime(n):
    if n<=0:
        return("Invalid Entry")
    
    elif n==1:
        return("not a prime num")
    
    for i in range(2, int(math.sqrt(n))+1): #2,3
        if n%i == 0:
            return("not a prime num")
    return("prime num")

n = int(input("Enter the number :"))
print(f"{n} is a {prime(n)}")