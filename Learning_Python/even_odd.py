num = int(input("Enter the number : "))
for i in range(1,num+1):
    if i % 2 == 0:
        print(f"The number {i} is even")
    else:
        print(f"The number {i} is odd")