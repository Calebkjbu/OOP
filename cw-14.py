class customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.emailid = ""
        self.balance = 0.0

    def add_new_customer(self):
        self.cid = input("What is the id?")
        self.acc_no = input("What is the account number?")
        self.cname = input("What is the name?")
        self.phone = input("What is the phone number?")
        self.emailid = input("What is the email?")
        self.balance = 100


    def credit_to(self):
        b1 = int(input("What is the amount transferred to you?"))
        self.balance += b1

    def debit_from(self):
        b2 = int(input("What is the amount transferred away from you?"))
        self.balance -= b2


    def display_all(self):
        print(self.cname)
        print(self.cid)
        print(self.acc_no)
        print(self.phone)
        print(self.emailid)
        print(self.balance)



c1 = customer()
c1.add_new_customer()

c2 = customer()
c2.add_new_customer()

c2.credit_to()
c1.debit_from()
c1.display_all()
c2.display_all()