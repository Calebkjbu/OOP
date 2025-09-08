myList = []
x = 0
while x==0:
    print("1.Append to the list")
    print("2.Remove from the list")
    print("3.pop an element form the list")
    print("4.Display the List")
    print("5.Quit")
    option = int(input("Chose your option?"))

    if option == 1:
       addToList = input("What would you like to add?")
       myList.append(addToList)
    elif option == 2:
       print(myList)
       RemList = input("What would you like to remove?")
       myList.remove(RemList)
    elif option == 3:
        x = len(myList) -1
        x  = myList[x]
        print("you are removing..", x)
        myList.pop()
    elif option == 4:
       for i in range (0,len(myList)):
           print(myList[i])
    elif option == 5:
       print("quitting...")
       x = 1
       break
    else :
       print("alright bud use one of the numbers ")


