#To convert a weight of a person from pounds to kilograms or vice-versa


weight = int(input("Enter your weight : "))
unit = input("(L)bs or (K)g : ")
if unit.upper() == "L":
    convered = weight * 0.45
    print(f"The converted weight is : {convered} kgs")
else:
    convered = weight/0.45
    print(f"You are {convered} pounds")