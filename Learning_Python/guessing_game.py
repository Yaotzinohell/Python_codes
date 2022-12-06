import random
secretnum = random.randint(1,9)
i = 0
while i < 3:
    num = int(input("Guess the number which is between 0 - 9 : "))
    if num == secretnum:
        print("You won")
        exit(0)
    i = i + 1
print("You failed")
print(f"The secret number was : {secretnum}")
exit(0)