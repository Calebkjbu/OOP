import pickle
class product:

    def __init__(self):
        self.pid = ""
        self.pname = ""
        self.price = 0.0
        self.desc = ""
    def get_product_details(self):
        self.pid = input("What is the product id?")
        self.pname = input("What is the product name?")
        self.price = float(input("What is the price in Dollars?"))
        self.desc = input("What is the description of the product?")

    def display_product_info(self):
        print(self.pid)
        print(self.pname)
        print(self.price)
        print(self.desc)

while 1:
    print("1.Create product obj")
    print("2.Get info from the product")
    print("3.Display the product")
    print("4.Write the product into file")
    print("5.read from the file")
    print("6.Exit")

    option = int(input("What option do you choose? "))

    if option == 1:
        product_obj = product()


    if option == 2:
        product_obj.get_product_details()

    if option ==3:
        product_obj.display_product_info()

    if option == 4:
        f1 = open("product_inv.dat", "ab")
        pickle.dump(product_obj,f1)
        f1.close()

    if option == 5:

        f2 = open("product_inv.dat", "rb")
        while 1:
            try:
                data = pickle.load(f2)
                print(data.display_product_info())
            except EOFError:
                break
