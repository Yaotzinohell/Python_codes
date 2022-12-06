n = int(input ("Enter the value: "))  
flag = 0
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag = 1
            print(f"{n} is a not prime number")
            break
if flag == 0:
    print(f"{n} is a prime number")
    print(f"The Prime Numbers from 0 to {n} are: ")  
    for num in range (0, n + 1):  
        if num > 1:  
            for i in range (2, num):  
                if (num % i) == 0:  
                    break  
            else:  
                print (num) 