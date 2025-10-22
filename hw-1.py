import pickle

while 1:
    print("1.Login")
    print("2.Quit")

    option = int(input("What option do you choose?"))

    if option == 1:
        usrname = input("whats the username?")
        file1 = open("passswordshw.dat", "rb")
        f1 = pickle.load(file1)
        i = 1
        for x in f1:
            var = "usr"+ str(i)
            print(file1[var]["uid"])
            i =+ 1

