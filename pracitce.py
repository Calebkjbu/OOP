name = input("What is your Name?")

wages = int(input("What is your hourly wage in dollars?"))
hours = int(input("how many hours per day do you work?"))
days = int(input("How many Days per week do you work?"))

monthly_wages= wages*hours*days * 52

print("You make ", monthly_wages, "dollars per year")
