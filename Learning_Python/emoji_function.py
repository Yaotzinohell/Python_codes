def emoji_converter(message):
    words = message.split(' ')  # Separates each word whenever a space occurs in a string
    emoji = {         #Create a dictionary
        ":)" : "😊",
        "XD" : "🤣",
        ":(" : "☹",
        "-_-": "😑"
    }
    out = ""
    for i in words:
        out = out + emoji.get(i,i) + " "
    return out

message = input(">")
print(emoji_converter(message))
