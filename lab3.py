class book:
    def __init__(self):
        self.book_Id = ""
        self.Title = ""
        self.Author = ""
        self.publisher = ""
        self.yrpub = ""



    def add_book(self):
        self.book_Id = input("What is the book ID?")
        self.Title = input("What is the books title?")
        self.publisher = input("What is the Publisher?")
        self.yrpub = input("What is the year of the publishing?")
    def display(self):
        print("Book ID: ",self.book_Id)
        print("Title: " , self.Title)
        print("Publisher: ", self.publisher)
        print("Year published", self.yrpub)
        print("Author: ", self.author.authorName)
    def add_author_tobook(self,aut):
        self.author = aut





class user:
    def __init__(self):
        self.user_ID = ""
        self.User_Name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.emailid = ""
        self.Books_Borrowed = []

    def create_user(self):
        self.user_ID = input("What is the User Id?")
        self.User_Name = input("What is the users name?")
        self.password = input("What is the password?")
        self.address = input("What is the address?")
        self.phone = input("What is your phone number?")
        self.emailid = input("What is your Email Id?")

    def borrow_book(self, bb):
        self.Books_Borrowed.append(bb)
    def display(self):
        print("User Id: ", self.user_ID)
        print("User Name: ", self.User_Name)
        print("Password: ", self.password)
        print("Address: ", self.address)
        print("Phone Num: ", self.phone)
        print("Email: ", self.emailid)
        for x in self.Books_Borrowed:
            print("Books Borrowed:", x.Title)


class Author:
    def __init__(self):
        self.authorid = ""
        self.authorName = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.emailid = ""

    def add_author(self):
        self.authorid = input("What is the author id?")
        self.authorName = input("What is the author name?")
        self.affiliation = input("What is the authors affiliation?")
        self.country = input("What is the country?")
        self.phone = input('What is the authors phone num?')
        self.emailid = input("What is the authors email?")


    def display(self):
        print("Authors id: ",self.authorid)
        print("Authors name: ", self.authorName)
        print("Affiliation: ", self.affiliation)
        print("Country: ", self.country)
        print("Phone num: ", self.phone)
        print("Email: ", self.emailid)

x = 1
u1 = user()
u2 = user()
b1 = book()
b2 = book()
a1 = Author()
a2 = Author()
while x == 1:

    print("1.Create a user")
    print("2.Add a book")
    print("3.Add an author")
    print("4.Display")
    print("5.Borrow Books")
    print("6.Quit")
    option = int(input("Choose option: "))

    if option == 1:
        print("1.Create User 1?")
        print("2.Create User 2?")
        rs = int(input("Which?: "))
        if rs == 1:
            u1.create_user()
        if rs == 2:
            u2.create_user()
    if option == 2:
        print("Create Book 1?")
        print("Create Book 2?")
        bp = int(input("Which?: "))
        if bp == 1:
            b1.add_book()
        if bp == 2:
            b2.add_book()
    if option == 3:
        print("1.Create Author 1?")
        print("2.Create Author 2?")
        ap = int(input("Which?: "))
        if ap == 1:
            a1.add_author()
        if ap == 2:
            a2.add_author()
    if option == 4:
        print("1.Dislpay Users?")
        print("2.Display Books?")
        print("3.Display Authors?")
        dp = int(input("Which?: "))
        if dp == 1:
            u1.display()
            u2.display()
        if dp == 2:
            b1.display()
            b2.display()
        if dp == 3:
            a1.display()
            a2.display()
    if option == 5:
        print("1.Add Books to user 1?")
        print("2.Add Books to user 2?")
        cd = int(input("Which?: "))
        if cd == 1:
            print("1.Book1? ", b1.Title)
            print("2.book2? ", b2.Title)
            bookpick = int(input("Which?: "))
            if bookpick == 1:
                u1.borrow_book(b1)
                u1.display()
            if bookpick == 2:
                u1.borrow_book(b2)
                u1.display()

        if cd == 2:
            print("1.Book1? ", b1.Title)
            print("2.book2? ", b2.Title)
            bookpick = int(input("Which?: "))
            if bookpick == 1:
                u2.borrow_book(b1)
                u2.display()
            if bookpick == 2:
                u2.borrow_book(b2)
                u2.display()
        if option == 6:
            break






