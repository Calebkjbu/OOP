class book:
    def __init__(self):
        self.book_Id = ""
        self.Book_Name = ""
        self.Title = ""
        self.Author = ""


    def add_book(self):
        self.book_Id = input("What is the book ID?")
        self.Book_Name = input("What is the book name?")
        self.Title = input("What is the books title?")
        self.Author = input("What is the Author?")




class user:
    def __init__(self):
        self.user_ID = ""
        self.User_Name = ""
        self.Books_Borrowed = []

    def create_user(self):
        self.user_ID = input("What is the User Id?")
        self.User_Name = input("What is the users name?")

    def borrow_book(self,bb):
        self.Books_Borrowed.append(bb)

u1 = user()
u1.create_user()
u2 = user()
u2.create_user()

b1 = book()
b1.add_book()

b2 = book()
b2.add_book()

b3 = book()
b3.add_book()

b4 = book()
b4.add_book()

b5 = book()

b5.add_book()

u1.borrow_book(b1)

u1.borrow_book(b2)

u2.borrow_book(b3)
u2.borrow_book(b4)

u2.borrow_book(b5)


