file1 = open("passwordshw-1.txt", "w")
x = 1
while x == 1:
    print("1.Login")
    print("2.Quit")

    option = int(input("What option do you choose?"))

    if option == 1:
        usrname = input("whats the username?")

        for x in file1:
            print(x)
