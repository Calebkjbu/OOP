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


a1 = Author()
a1.add_author()

a2 = Author()
a2.add_author()

u1 = user()
u1.create_user()

u2 = user()
u2.create_user()

b1 = book()
b1.add_book()
b1.add_author_tobook(a1)

b2 = book()
b2.add_book()
b2.add_author_tobook(a2)


u1.borrow_book(b1)
u1.borrow_book(b2)

u2.borrow_book(b1)

u1.display()
a1.display()
b1.display()


