import time

number1 = int(input("choose a number "))
number2 = int(input("choose another number"))
operator = input("Choose your operator (+,-,*,/)   ")

if operator == "+":
    print("the result is: ", number1 + number2)
elif operator == "-":
    print("the result is: ",number1 - number2)
elif operator == "*":
    print("the result is: ",number1 * number2)
elif operator == "/":
    print("the result is: ",number1/number2)
else:
    print("Why didn't you choose one of the operators listed mannnn, this aint cool")
    print("for not follwing instructions you get a consequnce")
    time.sleep(3)
    print("uninstalling OS and deleting system32....")