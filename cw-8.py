project = {}
x = 1
inp = 0
while x == 1:
    print("1.Initiate a new Project")
    print("2.Delete a project")
    print("3.Print a Project")
    print("4.Print all Projects")
    print("5.Quit")
    option = int(input("What option are you choosing"))

    if option == 1:
        addmanager = []
        addteam = []
        sidmaker = "s" + str(len(project) + 1)

        addtitle = input("What is the title for the project?")
        addstart = input("What is the start date?")
        addend = input("What is the end date")
        addsponsor = input("What is the sponsor that is sponsoring?")
        addbudget = int(input("What is the budget?"))
        addtech = input("What are the technologies?")

        addmanagernum = int(input("How many managers would you like to add?"))

        for i in range(0, addmanagernum):
            newmanager = input("What is the new manager?")
            addmanager.append(newmanager)

        addteamnum = int(input("How many Team Members would you like to add?"))

        for i in range(0, addteamnum):
            newteam = input("What is the new Team_Member?")
            addteam.append(newteam)

        project.update({sidmaker: {
            "Project_Title": addtitle,
            "Managers": [addmanager],
            "start_Date": addstart,
            "end_date": addend,
            "sponsor": addsponsor,
            "budget": addbudget,
            "technologies": addtech,
            "team_members": [addteam]
        }})

        print(project)
    elif option == 2:
        print(project)
        whatdel = input("What Project would you like to delete?(id)")
        del project[whatdel]
    elif option == 3:
        whaproject = input("What project would you like to print?(id)")
        print(project[whaproject])



