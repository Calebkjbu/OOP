p = int(input("What is the Principle loan amount?"))

R = int(input("What is the rate of intrest?"))

n = int(input("How long to you intened to take to repay the loan?"))

r = R/(12*100)
emi = p * r * ((1 +r)**n)/((1+r)**n-1)

print(emi)

for i in range (n,1,-1):
    output = p - emi
    p = output
    print(output, ":Balance")
    print(emi, ":EMI")
