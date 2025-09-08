import time
from idlelib.run import MyHandler

myList = []
z = 0
while z==0:
    print("1.Append to the list")
    print("2.Remove from the list")
    print("3.pop an element form the list")
    print("4.Display the List")
    print("5.Quit")
    option = int(input("Chose your option?"))

    if option == 1:
       addToList = input("What would you like to add?")
       myList.append(addToList)
       time.sleep(1)
    elif option == 2:
       x = len(myList)
       if x >= 1:
            print(myList)
            RemList = input("What would you like to remove?")
            myList.remove(RemList)
            time.sleep(1)
       else :
           print("there is nothing in the list")
           time.sleep(1)
    elif option == 3:
        x = len(myList)
        if x >= 1:
            y = len(myList) -1
            y  = myList[y]
            print("you are removing..", y)
            myList.pop()
            time.sleep(1)
        else:
            print("there is nothing in the list")
            time.sleep(1)
    elif option == 4:
       for i in range (0,len(myList)):
           print(myList[i])
           time.sleep(1)
    elif option == 5:
       print("quitting...")
       time.sleep(1)
       z = 1
       break
    else :
       print("alright bud use one of the numbers ")
       time.sleep(1)



