try:
    c = int(input("Enter the temperature in .c : "))
    f = (c*9/5)+32
    print(f"The temperature in Farenheit is {f}")
except Exception:
    print(f"Invalid entry")
