import time

myList = []
x = 0
while x==0:
    print("1.Append to the list")
    print("2.Remove from the list")
    print("3.Replace an Element from the list")
    print("4.Sort the elements in the list ")
    print("5.Reverse the elements in the list ")
    print("6.Print the list Elements")
    print("7.Quit")

    option = int(input("Chose your option?"))

    if option == 1:
       addToList = input("What would you like to add?")
       myList.append(addToList)
    elif option == 2:
       print(myList)
       RemList = input("What would you like to remove?")
       myList.remove(RemList)
    elif option == 3:
        print("Contents are:")
        for i in range(0, len(myList)):
            print(i, ". ", myList[i])
        repList = int(input("What is the index of the item to be replaced?"))
        new_Item = input("What would you like to replace it with?")
        myList[repList] = new_Item
        print("New Elements are:")
        for i in range(0, len(myList)):
            print(myList[i])
        time.sleep(1)
    elif option == 4:
        print("Before Sort:")
        for i in range(0, len(myList)):
            print(myList[i])
        time.sleep(1)
        myList.sort()
        print("After Sort:")
        for i in range(0, len(myList)):
            print(myList[i])
        time.sleep(1)

    elif option == 5:
        print("Before Reverse:")
        for i in range(0, len(myList)):
            print(myList[i])
        time.sleep(1)
        myList.reverse()
        print("After Reverse:")
        for i in range(0, len(myList)):
            print(myList[i])
        time.sleep(1)
    elif option == 6:
       for i in range (0,len(myList)):
           print(myList[i])
       time.sleep(1)
    elif option == 7:
       print("quitting...")
       x = 1
       break
    else:
       print("alright bud use one of the numbers ")


