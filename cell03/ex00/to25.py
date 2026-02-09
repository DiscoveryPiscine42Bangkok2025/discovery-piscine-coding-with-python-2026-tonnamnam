number = int(input("Enter number less than 25\n"))
if number > 25:
    print("Error")
else:
    for i in range(number , 26):
        print("Inside the loop, my variable is", i)