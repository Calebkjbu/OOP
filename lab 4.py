class customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.emailid = ""
        self.credit_card = []
        self.debit_card = ""
        self.transfer_amount = ""
        self.withdrawl = ""

    def add_new_customer(self):
        self.cid = input("What is the id?")
        self.acc_no = input("What is the account number?")
        self.cname = input("What is the name?")
        self.phone = input("What is the phone number?")
        self.emailid = input("What is the email?")




    def credit_to(self,tran):
        i = 1
        print(self.cname, "Choose What card to add to")
        for x in self.credit_card:
            print(str(i), x.card_no)
            i += 1
        choice = int(input("??"))
        if choice == 1:
            self.credit_card[0].balance += tran
            print(self.credit_card[0].balance)
        elif choice == 2:
            self.credit_card[1].balance += tran
            print(self.credit_card[1].balance)



    def debit_from(self,tran):

        print(self.cname,"The amount that is being withdarwn is" , str(tran))
        self.debit_card.balance -= tran
        print("Balance left after transaction",self.debit_card.balance)





    def display_all(self):
        print(self.cname)
        print(self.cid)
        print(self.acc_no)
        print(self.phone)
        print(self.emailid)

    def add_credit_card_customer(self,cc):
        self.credit_card.append(cc)

    def add_Debit_card(self,cd):
        if self.debit_card == "":
            self.debit_card = cd

        else:
            print("Cant add card, there is already a debit on this account")

class card:
    def __init__(self):
        self.Crtype = ""
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = ""


    def addCard(self):

        print("Is it")
        print("1.Debit?")
        print("2.Credit?")
        self.Crtype = int(input("Choose number.."))
        self.card_no = int(input("What is the card number"))
        self.cvv = int(input("What is the cvv code?"))
        self.expiry_date = int(input("what is the expiration date?"))
        self.balance = int(input("What is the balance on this card?"))

    def display_card(self):

        if self.Crtype == 1:
            print("Debit")

        elif self.Crtype == 2:
            print("Credit")

        print(self.card_no)
        print(self.cvv)
        print(self.expiry_date)
        print(self.balance)

c1 = customer()
c1.add_new_customer()

c2 = customer()
c2.add_new_customer()

cr1 = card()
cr1.addCard()

cr2 = card()
cr2.addCard()

cr3 = card()
cr3.addCard()

c1.add_credit_card_customer(cr1)
c1.add_credit_card_customer(cr2)


c2.add_Debit_card(cr3)

c1.credit_to(1000)
c2.debit_from(1000)




