x = 0
while x==0:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit")
    option = int(input("Select an option:? "))

    if option == 1:
        n1 = int(input("whats the first number? "))
        n2 = int(input("whats the second number? "))
        n3 = n1 +n2
        print("The result is ", n3)

    elif option == 2:
        n1 = int(input("whats the first number? "))
        n2 = int(input("whats the second number? "))
        n3 = n1 - n2
        print("The result is ", n3)
    elif option == 3:
        n1 = int(input("whats the first number? "))
        n2 = int(input("whats the second number? "))
        n3 = n1 * n2
        print("The result is ", n3)
    elif option == 4:
        n1 = int(input("whats the first number? "))
        n2 = int(input("whats the second number? "))
        n3 = n1 / n2
        print("The result is ", n3)
    elif option == 5:
        x = 1
        break
