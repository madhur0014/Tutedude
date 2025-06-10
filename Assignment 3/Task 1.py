n=int(input("Enter a number:"))
def Factorial(n):
    if n<2:
        return 1
    else:
        return n*(Factorial(n-1))
print("Factorial of",n,"is:",Factorial(n))
