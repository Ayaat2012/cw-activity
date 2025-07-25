# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1:
        return n
    
    else:
        return n*recur_factorial(n-1)
    
num = int(input("Enter a number"))

# Check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative integers")

elif num == 0:
    print("The factorial for 0 is 1.")

else:
    print("The factorial of", num , "is", recur_factorial(num))