list = []
x =1
def enqueue():
    addvar = input("What would you like to add to the queue")
    list.append(addvar)
def dequeue():
    rem = list[0]
    list.remove(rem)
def display():
    print(list)


while x == 1:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Quit")

    option = int(input("What is the option you choosin? : "))

    if option == 1:
        enqueue()
    elif option == 2:
        dequeue()
    elif option == 3:
        display()
    elif option == 4:
        print("quiting....")
        break
    else:
        print("BOOHOO BUD")
        break
