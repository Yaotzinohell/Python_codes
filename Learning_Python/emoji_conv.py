message = input(">")
words = message.split(' ')  # Separates each word whenever a space occurs in a string
emoji = {         #Create a dictionary
    ":)" : "😊",
    "XD" : "🤣",
    ":(" : "☹",
    "-_-": "😑"
}
out =""
for i in words:
    out = out + emoji.get(i,i) + " "   #i,i is used to give the default value if the emoji is not used
print(out)