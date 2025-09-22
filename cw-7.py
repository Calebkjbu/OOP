dictionary = {}
x = 1

while x == 1:
    print("What operation would you like to accomplish?")
    print("1.Add a Student")
    print("2.Delete a Student")
    print("3.Edit a Student")
    print("4.Print a student")
    print("5.Quit")

    option = int(input("What is the option?"))

    if option == 1:
        addStudent = input("What is the name of the student?")
        addMajor = input("What major?")
        addYear = input("What Year?")
        addCredits = input("How many credits?")
        addGpa = input("What is the GPA?")
        length = len(dictionary) + 1

        nameAdder = "s"+str(length)

        dictionary.update({nameAdder: {
            "name": addStudent,
            "major": addMajor,
            "year": addYear,
            "credits": addCredits,
            "GPA": addGpa
        }})
        print(dictionary)
    elif option == 2:
        delStudent = input("What student would you like to delete?(give ID)")
        print(dictionary)
        del dictionary[delStudent]
        print(dictionary)
    elif option == 3:
        print(dictionary)
        editStudent = input("What Student would you like to edit?(Give Id)")
        newName = input("Give name")
        newMajor = input("Give Major")
        newYear = input("Give Year")
        newCredits = input("Give Credits")
        newGpa = input("Give GPA")
        dictionary.update({editStudent: {
            "name": newName,
            "major": newMajor,
            "year": newYear,
            "credits": newCredits,
            "GPA": newGpa
        }})
        print(dictionary)
    elif option == 4:
        print(dictionary)
    elif option == 5:
        x = 0
        break
