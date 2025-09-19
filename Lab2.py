myStudents = {}

x = 0

while x == 0:
    print("Hello, Choose an option from the list below")
    print("1.Add Student")
    print("2.Delete Student")
    print("3.Modify a Student")
    print("4.Display all the Students ")
    print("5.Quit")

    option = int(input("What option number?"))

    if option == 1:
        addStudent = input("What is the name of the student?")
        addlab1 = int(input("Points for lab 1 "))
        addlab2 = int(input("Points for lab 2 "))
        addlab3 = int(input("Points for lab 3 "))
        addlab4 = int(input("Points for lab 4 "))
        addlab5 = int(input("Points for lab 5 "))
        length = len(myStudents) + 1
        avgscr = (addlab1 + addlab2 + addlab3 + addlab4 + addlab5)/5
        prc = avgscr /50 *100
        IDcreate = "s"+str(length)

        myStudents.update({IDcreate:{
            "name": addStudent,
            "lab1": addlab1,
            "lab2": addlab2,
            "lab3": addlab3,
            "lab4": addlab4,
            "lab5": addlab5,
            "Avg": avgscr,
            "Score": prc


        }})
    elif option == 2:
        print(myStudents)
        delStudent = input("What is the Id of the student you would like to delete ")
        del myStudents[delStudent]
    elif option == 3:
        print(myStudents)
        modStu = input("What Student would you like to modify?")
        newName = input("What is the new name for the student?")
        newlab1 = int(input("What is the new lab 1 score"))
        newlab2 = int(input("What is the new lab 2 score"))
        newlab3 = int(input("What is the new lab 3 score"))
        newlab4 = int(input("What is the new lab 4 score"))
        newlab5 = int(input("What is the new lab 5 score"))
        avgscr = (newlab1 + newlab2 + newlab3 + newlab4 + newlab5)/5
        prc = avgscr /50 *100
        myStudents.update({modStu: {
            "name": newName,
            "lab1": newlab1,
            "lab2": newlab2,
            "lab3": newlab3,
            "lab4": newlab4,
            "lab5": newlab5,
            "Avg": avgscr,
            "Score": prc

        }})
    elif option == 4:
        print("Displaying the students and their score")
        print(myStudents)
    elif option == 5:
        x = 1
        break