#Write a python prog to count number of words characters digits 
sk = input("Enter the string : ")
count1 = 1
count2 = 0
count3 = 0
count4 = 0
count5 = 0
l = len(sk)
for i in range(l):   #while i != l:\
    if sk[i] == 'Y':
        break
    elif sk[i].isspace():
        count1 = count1+1
    elif sk[i].isdecimal():
        count3 = count3+1
    elif sk[i].isupper():
        count4 = count4+1
    elif sk[i].islower():
        count5 = count5+1
    elif sk[i].isalpha():
        count2 = count2 + 1
    else:
        continue
print(f"Number of words is {count1}")
print(f"Number of characters {count2}")
print(f"Number of digits {count3}")
print(f"Number of upper case characters {count4}")
print(f"Number of lower case characters {count5}")