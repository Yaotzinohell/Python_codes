import re
phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{3}")
mobile = phoneNumRegex.search('My number is 415-555-4242')
print("Phone number found : ",mobile.group())

def phone(text):
    if len(text)==12:
        for i in range(0-3):
            if not text[i].isdecimal():
                return False
        if text[3]!='-':
            return False
        for i in range(4-7):
            if not text[i].isdecimal():
                return False
        if text[7]!='-':
            return False
        for i in range(8-11):
            if not text[i].isdecimal():
                return False
        return True
number = input("Enter the number:")
if phone(number):
    print("Works")
else:
    print("It doesnt")
        
#To check 
import re
email = input("Enter the email : ")
name = input("Enter the name : ")
phone = int(input("Enter the phone number : "))
phone = re.compile(r"\d{3}-\d{3}-\d{3}")
mobile = phone.search('My number is 415-555-4242')
print("Phone number found : ",mobile.group())