try:
    age = [10,20,30]
    tattoo = int(input("Enter 0 : "))
    flow = age[1]/tattoo
    print(age[0])
    print(flow)
except ZeroDivisionError:
    print("Age cannot be 0")
except IndexError:
    print("Invalid Entry")
numbers = [1,2,3]
