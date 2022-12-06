com = ""
count1 = 0
count2 = 0
while True:
    com = input("> ").lower()
    if com == "start":
        count2 = 0
        if count1 == 0:
            count1 = count1 + 1
            print("The car Started...")
        else:
            print("Car already started")
    elif com == "stop":
        count1 = 0
        if count2 == 0:
            count2 = count2 + 1
            print("Car stopped.......")
        else:
            print("Car already stopped")
    elif com == "help":
        print('''
        start -  to start the car
        stop - to stop the car
        quit - to quit
        ''')
    elif com == "quit":
        break
    else:
        print("Sorry i dont understand")
