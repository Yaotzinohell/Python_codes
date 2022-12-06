#To check 
import re
email = input("Enter the email : ")
name = input("Enter the name : ")
phone = int(input("Enter the phone number : "))
phone = re.compile(r"\d{3}-\d{3}-\d{3}")