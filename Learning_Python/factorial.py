def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter the number to find the factorial : "))
print(f"The Factorial of the number {n} is {fact(n)}")