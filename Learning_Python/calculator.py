def add(a,b):
    sum = 0
    sum = a + b
    return sum
def sub(a,b):
    diff=0
    diff = a - b
    return diff
def mul(a,b):
    mul = a * b
    return mul
def div(a,b):
    div = a / b
    return div
while(True):
    print("Press\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Exit The Program")
    ch = int(input("Enter your choice : "))
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    if ch == 1:
        print(f"Addition of {a} and {b} is {add(a,b)}")
        break
    elif ch == 2:
        print(f"Subtraction of {a} and {b} is {sub(a,b)}")
        break
    elif ch == 3:
        print(f"Multiplication of {a} and {b} is {mul(a,b)}")
        break
    elif ch == 4:
        print(f"Division of {a} and {b} is {div(a,b)}")
        break
    elif ch == 5:
        exit(0)
    else:
        print("Try again")
